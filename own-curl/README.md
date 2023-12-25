# Write Your Own curl
Usage:
```
usage: ccurl.py [-h] [-v] [-x METHOD] [-j JSON] URL

Custom cURL

positional arguments:
  URL                   URL to fetch

options:
  -h, --help            show this help message and exit
  -v, --verbose         Enable verbose mode
  -x METHOD, --method METHOD
                        HTTP method
  -j JSON, --json JSON  JSON payload for POST
```

Example 1
```
% python3 ccurl.py -x get http://eu.httpbin.org/get -v

Connecting to eu.httpbin.org port 80

> GET /get HTTP/1.1
> Host: eu.httpbin.org
> Connection: close

< HTTP/1.1 200 OK
< Date: Mon, 25 Dec 2023 06:44:55 GMT
< Content-Type: application/json
< Content-Length: 204
< Connection: close
< Server: gunicorn/19.9.0
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Credentials: true
< 
< {
  "args": {}, 
  "headers": {
    "Host": "eu.httpbin.org", 
    "X-Amzn-Trace-Id": "Root=1-658924e7-50e2da4d399e069a0f8fa089"
  }, 
  "origin": "110.224.82.36", 
  "url": "http://eu.httpbin.org/get"
}

```

Example 2
```
% python3 ccurl.py -x post http://eu.httpbin.org/post  -j data.json

Connecting to eu.httpbin.org port 80

{
  "args": {}, 
  "data": "{\n    \"name\": \"John Doe\",\n    \"age\": 30,\n    \"city\": \"New York\",\n    \"email\": \"john.doe@example.com\",\n    \"is_student\": false,\n    \"grades\": [85, 90, 78, 92]\n  }\n  ", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Content-Length": "164", 
    "Content-Type": "application/json", 
    "Host": "eu.httpbin.org", 
    "X-Amzn-Trace-Id": "Root=1-65892d53-11e2a7346acf34d312675abf"
  }, 
  "json": {
    "age": 30, 
    "city": "New York", 
    "email": "john.doe@example.com", 
    "grades": [
      85, 
      90, 
      78, 
      92
    ], 
    "is_student": false, 
    "name": "John Doe"
  }, 
  "url": "http://eu.httpbin.org/post"
}

```