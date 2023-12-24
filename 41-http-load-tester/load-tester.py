import httpx
import asyncio
import argparse
import time

async def perform_load_test(url,num_requests,concurrent_requests,http_method):
    total_rounds = int(num_requests/concurrent_requests)
    
    # the ones with status code 200,300
    success = 0
    # the ones with status code 400,500
    failure = 0
    
    ttfb = []
    total_times = []
    
    for _ in range(total_rounds):
        async with httpx.AsyncClient() as client:
            tasks = []
            for _ in range(concurrent_requests):
                start_time = time.time()
                task = client.get(url)
                tasks.append((start_time, task))

            results = await asyncio.gather(*[task[1] for task in tasks])

            for start_time, result in zip(tasks, results):
                status = int(result.status_code / 100)
                end_time = time.time()
                total_time = end_time - start_time[0]
                ttfb_time = result.elapsed.total_seconds()

                ttfb.append(ttfb_time)
                total_times.append(total_time)

                if status == 2 or status == 3:
                    success += 1
                else:
                    failure += 1

    print("Results....")
    print("Successful requests (2xx, 3xx):", success)
    print("Failed requests (4xx, 5xx):", failure)
    print("Time to First Byte (TTFB):", ttfb)
    print("Total Time:", total_times)
    
    
async def main():
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
    await perform_load_test(url,num_requests,concurrent_requests,http_method)

if __name__ == "__main__":
    asyncio.run(main())
    