from fastapi import FastAPI,Request
from starlette.middleware.base import BaseHTTPMiddleware
from token_bucket import token_bucket_middleware



app = FastAPI()

my_middleware = token_bucket_middleware()
app.add_middleware(BaseHTTPMiddleware,dispatch=my_middleware)

@app.get("/unlimited")
async def unlimited():
    return {"message": "Unlimited! Let's Go!"}

@app.get("/limited")
async def limited():
    return {"message": "Limited, don't overuse me!"}
