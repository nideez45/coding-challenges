import socket
import argparse
from urllib.parse import urlparse

def make_request(url,verbose,method):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    parsed_url = urlparse(url)
    protocol = parsed_url.scheme
    hostname = parsed_url.hostname
    path = parsed_url.path
    if not path:
        path = '/'
    query = parsed_url.query

    port = 0
    if protocol == 'http':
        port = 80
    elif protocol == 'https':
        port = 443
    else:
        print("Unknown protocol")
        exit()
        
    print("Connecting to {} port {}".format(hostname,port))
    print()
    
    client_socket.connect((hostname,port))
    # create the http content
    
    request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\n"
    headers = {'Connection':'close'}
    if headers:
        request += "\r\n".join([f"{key}: {value}" for key, value in headers.items()]) + "\r\n"
    request += "\r\n"
    if verbose:
        request_lines = request.split("\r\n")
        print("> " + "\r\n> ".join(request_lines[:-2]))
        print()
    client_socket.sendall(request.encode('utf-8'))
    response = client_socket.recv(4096).decode("utf-8")
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

def main():
    parser = argparse.ArgumentParser(description='Custom cURL')
    parser.add_argument('url', metavar='URL', type=str, help='URL to fetch')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    parser.add_argument('-x', '--method', type=str, metavar='METHOD', help='HTTP method')

    args = parser.parse_args()

    # Access the values
    url = args.url
    verbose = args.verbose
    method = args.method

    if method.lower() != 'get':
        print("Currently only works for GET")
        exit()

    make_request(url,verbose,method)


if __name__ == '__main__':
    main()