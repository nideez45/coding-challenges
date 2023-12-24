# Write Your Own HTTP(S) Load Tester
Usage:
```
usage:python3 load-tester.py [-h] -u URL [-n N] [-c C] -m METHOD

Http load tester

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to test
  -n N                  Number of requests
  -c C                  Number of concurrent users
  -m METHOD, --method METHOD
                        HTTP method (e.g., get,post)
```
Example:
```
% python3 load-tester.py -u https://google.com -n 10 -c 10 -m GET

Load testing: https://google.com
Total request made 10
Concurrent users: 10


Results....
Total time taken (s) :  1.87
Successful requests (2xx, 3xx)..............: 10
Failed requests (4xx, 5xx)..................: 0
Total Request Time (s) (Min, Max, Mean).....: 0.94 , 1.49 , 1.22
Time to First Byte (s) (Min, Max, Mean).....: 0.69 , 1.31 , 0.94
Time to Last Byte (s) (Min, Max, Mean)......: 0.05 , 0.57 , 0.27
```
