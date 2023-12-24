

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
    
    def printStats(self,total):
        print("Results....")
        print("Total time taken (s) : ",round(total,2))
        print("Successful requests (2xx, 3xx)..............:", self.success)
        print("Failed requests (4xx, 5xx)..................:", self.failure)
        print("Total Request Time (s) (Min, Max, Mean).....:", round(self.total_times[0],2),",",round(self.total_times[1],2),",", round(self.total_times[2]/self.total_request,2))
        print("Time to First Byte (s) (Min, Max, Mean).....:", round(self.ttfb[0],2),",", round(self.ttfb[1],2), ",",round(self.ttfb[2]/self.total_request,2))
        #print("Time to Last Byte (s) (Min, Max, Mean)......:", round(self.ttlb[0],2),",", round(self.ttlb[1],2), ",",round(self.ttlb[2]/self.total_request,2))