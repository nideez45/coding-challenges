import socket
import argparse
from urllib.parse import urlparse

def make_request(url,verbose,method):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    parsed_url = urlparse(url)
    protocol = parsed_url.scheme
    hostname = parsed_url.hostname
    path = parsed_url.path
    query = parsed_url.query

    print(f"Protocol: {protocol}")
    print(f"Hostname: {hostname}")
    print(f"Path: {path}")
    print(f"Query: {query}")
    print()
    port = 0
    if protocol == 'http':
        port = 80
    elif protocol == 'https':
        port = 443
    else:
        print("Unknown protocol")
        exit()
    client_socket.connect((hostname,port))
    # create the http content
    
    request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\n"
    headers = None
    if headers:
        request += "\r\n".join([f"{key}: {value}" for key, value in headers.items()]) + "\r\n"
    request += "\r\n"
    
    client_socket.sendall(request.encode('utf-8'))
    response = client_socket.recv(4096).decode("utf-8")
    print(response)

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

    # Print the values for demonstration
    print(f"URL: {url}")
    print(f"Verbose: {verbose}")
    print(f"HTTP Method: {method}")
    print()
    make_request(url,verbose,method)


if __name__ == '__main__':
    main()