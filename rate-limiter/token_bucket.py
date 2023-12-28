from fastapi import Request

class token_bucket_middleware:
    async def __call__(self, request: Request, call_next):
        print("Middleware A - Request Phase")
        response = await call_next(request)
        print("Middleware A - Response Phase")
        return response