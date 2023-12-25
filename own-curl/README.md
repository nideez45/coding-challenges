# Write Your Own curl
Usage:
```
usage: ccurl.py [-h] [-v] [-x METHOD] URL

Custom cURL

positional arguments:
  URL                   URL to fetch

options:
  -h, --help            show this help message and exit
  -v, --verbose         Enable verbose mode
  -x METHOD, --method METHOD
                        HTTP method
```

Example
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