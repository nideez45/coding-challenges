
from connection import make_connection

def make_get_request(url,verbose):
    path,hostname,client_socket = make_connection(url)
    
    request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\n"
    headers = {'Connection':'close','Cache-Control': 'no-cache'}
    if headers:
        request += "\r\n".join([f"{key}: {value}" for key, value in headers.items()]) + "\r\n"
    request += "\r\n"
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