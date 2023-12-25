import argparse
from urllib.parse import urlparse
from get import make_get_request
from delete import make_delete_request


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

    

    if method == 'get':
        make_get_request(url,verbose)
    elif method == 'delete':
        make_delete_request(url,verbose)
    else:
        print("Currently {} is not supported".format(method))
        exit()

if __name__ == '__main__':
    main()