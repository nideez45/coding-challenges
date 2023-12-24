import requests
import asyncio
import argparse
import time

class Statistics:
    def __init__(self,total_request) -> None:
        self.success = 0
        self.failure = 0
        self.ttfb = [100,-1,0]
        self.ttlb = [100,-1,0]
        self.total_times = [100,-1,0]
        self.total_request = total_request
    
    def updateTTFB(self,value):
        self.ttfb[2]+=value
        if self.ttfb[0]>value:
            self.ttfb[0] = value
        if self.ttfb[1]<value:
            self.ttfb[1] = value
            
    def updateTTLB(self,value):
        self.ttlb[2]+=value
        if self.ttlb[0]>value:
            self.ttlb[0] = value
        if self.ttlb[1]<value:
            self.ttlb[1] = value
            
    def updateTotalTime(self,value):
        self.total_times[2]+=value
        if self.total_times[0]>value:
            self.total_times[0] = value
        if self.total_times[1]<value:
            self.total_times[1] = value  
    
    def printStats(self):
        print("Results....")
        print("Successful requests (2xx, 3xx)..............:", self.success)
        print("Failed requests (4xx, 5xx)..................:", self.failure)
        print("Total Request Time (s) (Min, Max, Mean).....:", round(self.total_times[0],2),",",round(self.total_times[1],2),",", round(self.total_times[2]/self.total_request,2))
        print("Time to First Byte (s) (Min, Max, Mean).....:", round(self.ttfb[0],2),",", round(self.ttfb[1],2), ",",round(self.ttfb[2]/self.total_request,2))
        print("Time to Last Byte (s) (Min, Max, Mean)......:", round(self.ttlb[0],2),",", round(self.ttlb[1],2), ",",round(self.ttlb[2]/self.total_request,2))
        
        
async def simulate_user(url,http_method,stats:Statistics):
    if http_method == 'get':
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        total_time = end_time-start_time
        ttfb = response.elapsed.total_seconds()
        ttlb = total_time-ttfb
        stats.updateTTFB(ttfb)
        stats.updateTTLB(ttlb)
        stats.updateTotalTime(total_time)
        status = int(response.status_code / 100)
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
    
    print("Load testing:" ,url)
    print("Total request made",num_requests)
    print("Concurrent users:",concurrent_requests)
    print()
    print()
    global sem
    sem = asyncio.Semaphore(concurrent_requests)
    stats = Statistics(num_requests)
    tasks = [safe_simulate_user(url,http_method,stats) for _ in range(num_requests)]
    await asyncio.gather(*tasks)
    stats.printStats()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
    