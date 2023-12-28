from fastapi import Request
import time
from fastapi.responses import JSONResponse


class token_bucket_middleware:
    bucket = {}
    def __init__(self,capacity:int,tps:float) :
        self.capacity = capacity
        self.tps = tps
       
    
    async def refill_bucket(self,client_ip):
        cur_time = time.time()
        diff = cur_time-self.bucket[client_ip][1]
        to_add = ((diff//1)*self.tps)//1
        self.bucket[client_ip][0] = min(self.bucket[client_ip][0]+to_add,self.capacity)
    
    async def __call__ (self, request: Request, call_next):
        client_ip = request.client.host
        if client_ip not in self.bucket.keys():
            self.bucket[client_ip] = [self.capacity,time.time()]
            
        await self.refill_bucket(client_ip)
        if self.bucket[client_ip][0]>0:
            self.bucket[client_ip][0] -= 1
            self.bucket[client_ip][1] = time.time()
            return await call_next(request)
        
        content = "Rate limit exceeded. Too many requests"
        return JSONResponse(content=content, status_code=429)

    