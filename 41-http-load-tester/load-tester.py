import httpx
import asyncio
import argparse



def main():
    parser = argparse.ArgumentParser(description='Http load tester')
    
    # Required arguments
    parser.add_argument('-u', '--url', type=str, help='URL to test', required=True)
    
    # Optional arguments with default values
    parser.add_argument('-n', type=int, default=1, help='Number of requests')
    parser.add_argument('-c', type=int, default=1, help='Number of concurrent requests')
    
    parser.add_argument('-m', '--method', type=str, help='HTTP method (e.g., get)', required=True)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values
    url = args.url
    num_requests = args.n
    concurrent_requests = args.c
    http_method = args.method.lower()
    
    if http_method != 'get':
        print("Only GET supported for now!")
        exit()
    
    print(url,num_requests,concurrent_requests,http_method)
    #perform_load_test(url,num_requests,concurrent_requests,http_method)

if __name__ == "__main__":
    main()
    