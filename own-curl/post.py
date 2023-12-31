
import json
from connection import make_connection

def make_post_request(url,verbose,json_filename):
    
    path,hostname,client_socket = make_connection(url)
    
    request = f"POST {path} HTTP/1.1\r\nHost: {hostname}\r\n"
    
    try:
        with open(json_filename, 'r') as json_file:
            json_content = json_file.read()
    except FileNotFoundError:
        print(f"Error: File '{json_filename}' not found.")
        exit()
        
    headers = {'Connection':'close',"Content-Type":'application/json','Content-Length': str(len(json_content))}
    if headers:
        request += "\r\n".join([f"{key}: {value}" for key, value in headers.items()]) + "\r\n"
    request += "\r\n"
    
    request+=json_content
    
    if verbose:
        request_lines = request.split("\r\n")
        print("> " + "\r\n> ".join(request_lines[:-2]))
        print()
    client_socket.sendall(request.encode('utf-8'))
    
    response = ''
    while True:
        chunk = client_socket.recv(4096).decode("utf-8")
        if not chunk:
            break
        response += chunk
    
    if verbose:
        print("< " + response.replace("\r\n", "\r\n< "))
    else:
        # print only the response body ignoring the response headers
        double_crlf_index = response.find('\r\n\r\n')
    
        if double_crlf_index != -1:
            response_body = response[double_crlf_index + 4:]
            print(response_body)
        else:
            print("Invalid response format (missing double CRLF)")
    client_socket.close()