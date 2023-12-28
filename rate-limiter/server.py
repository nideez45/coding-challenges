from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from token_bucket import token_bucket_middleware

class TokenBucketMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path == "/limited":
            my_middleware = token_bucket_middleware(1, 1)

            return await my_middleware(request, call_next)
        else:
            return await call_next(request)


app = FastAPI()

app.add_middleware(TokenBucketMiddleware)

@app.get("/unlimited")
async def unlimited():
    return "Unlimited! Let's Go!"

@app.get("/limited")
async def limited():
    return "Limited, don't overuse me!"
