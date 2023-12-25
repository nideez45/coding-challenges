import socket
import ssl 
from urllib.parse import urlparse

def make_connection(url):
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
    
    
    
    if port == 443:
        client_socket = socket.create_connection((hostname,port))
        context = ssl.create_default_context()
        secure_socket = context.wrap_socket(client_socket, server_hostname=hostname)
        client_socket = secure_socket
    else:
        client_socket.connect((hostname,port))
    return path,hostname,client_socket