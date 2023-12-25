import socket
import argparse
from urllib.parse import urlparse
from get import make_get_request


def main():
    parser = argparse.ArgumentParser(description='Custom cURL')
    parser.add_argument('url', metavar='URL', type=str, help='URL to fetch')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    parser.add_argument('-x', '--method', type=str, metavar='METHOD', help='HTTP method')

    args = parser.parse_args()

    # Access the values
    url = args.url
    verbose = args.verbose
    method = args.method.lower()

    if method != 'get':
        print("Currently only works for GET")
        exit()

    if method == 'get':
        make_get_request(url,verbose)


if __name__ == '__main__':
    main()