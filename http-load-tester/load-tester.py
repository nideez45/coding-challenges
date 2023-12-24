import aiohttp
import asyncio
import argparse
import time

from statistics import Statistics

request_start = {}

async def on_request_start(
        session, trace_config_ctx, params):
    print("request started")
    request_start['time'] = time.time()
    print(time.time())

async def simulate_user(url,http_method,stats:Statistics):
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_chunk_sent.append(on_request_start)

    if http_method == 'get':
        start_time = time.time()
        print(start_time)
        async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
            response = await session.get(url)
            await response.content.readexactly(1)
            ttfb = time.time() - request_start['time']
            await response.content.read()
            ttlb = time.time() - request_start['time']
        end_time = time.time()
        print(end_time)
        total_time = end_time-start_time
        
        stats.updateTTFB(ttfb)
        stats.updateTTLB(ttlb)
        stats.updateTotalTime(total_time)
        status = int(response.status / 100)
        if status == 2 or status == 3:
            stats.success+=1
        else:
            stats.failure+=1
    
   
async def safe_simulate_user(url,method,stats):
    async with sem:
        return await simulate_user(url,method,stats)

async def main():
    parser = argparse.ArgumentParser(description='Http load tester')
    
    # Required arguments
    parser.add_argument('-u', '--url', type=str, help='URL to test', required=True)
    
    # Optional arguments with default values
    parser.add_argument('-n', type=int, default=1, help='Number of requests')
    parser.add_argument('-c', type=int, default=1, help='Number of concurrent users')
    
    parser.add_argument('-m', '--method', type=str, help='HTTP method (e.g., get,post)', required=True)

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
    
    print("Load testing:" ,url)
    print("Total request made",num_requests)
    print("Concurrent users:",concurrent_requests)
    print()
    print()
    global sem
    sem = asyncio.Semaphore(concurrent_requests)
    stats = Statistics(num_requests)
    tasks = [asyncio.ensure_future(safe_simulate_user(url,http_method,stats)) for _ in range(num_requests)]
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()
    stats.printStats(end_time-start_time)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
    