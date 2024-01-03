from fastapi import FastAPI, HTTPException,Request
from pydantic import BaseModel
from starlette.responses import RedirectResponse
import hashlib
import starlette.status as status
import redis
app = FastAPI()

redis_client = None

class ShortenPayload(BaseModel):
    url: str 

@app.on_event("startup")
async def startup_event():
    global redis_client
    redis_client = redis.StrictRedis(host='localhost', port=6379)

def generate_short_url(original_url):
    
    short_url = redis_client.get(original_url)
    if short_url:
        return short_url
    
    hash_object = hashlib.sha256(original_url.encode())
    hash_hex = hash_object.hexdigest()
    short_url = hash_hex[:8]
    redis_client.set(original_url,short_url)
    redis_client.set(short_url,original_url)
    return short_url

@app.post("/shortenurl")
def shorten_url(payload:ShortenPayload):
    original_url = payload.url
    print(original_url)
    if original_url.startswith("http"):
        original_url=  original_url.split('://', 1)[-1]
    short_url = generate_short_url(original_url)
    print(short_url)
    return {"short_url": short_url}

@app.get("/{short_url}")
def redirect_url(short_url: str,request:Request):
    if len(short_url) != 8:
        raise HTTPException(status_code=404, detail="Short URL not found")
    original_url = redis_client.get(short_url)
    if original_url:
        return RedirectResponse(
        url="https://{}".format(original_url.decode()), status_code=status.HTTP_302_FOUND
    )
    else:
        raise HTTPException(status_code=404, detail="Short URL not found")
