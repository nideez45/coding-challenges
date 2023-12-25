# Write Your Own Traceroute
Usage
```
usage: ctraceroute.py [-h] domain

Custom traceroute

positional arguments:
  domain      Domain to traceroute for

options:
  -h, --help  show this help message and exit
```
Example
```
% sudo python3 ctraceroute.py google.com
Traceroute to google.com (142.250.193.110)... max 30 hops
1 _gateway ( 192.168.43.1 ) 47.92 ms
2 * * *
3 * * *
4 * * *
5 * * *
6 * * *
7 * * *
8 nsg-static-113.206.71.182.airtel.in ( 182.71.206.113 ) 81.15 ms
9 * * *
10 * * *
11 * * *
12 * * *
13 * * *
14 * * *
15 * * *
16 * * *
17 * * *
18 maa05s24-in-f14.1e100.net ( 142.250.193.110 ) 83.47 ms
```