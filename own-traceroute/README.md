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
1 _gateway ( 192.168.43.1 )
2 * * *
4 * * *
6 * * *
5 192.168.31.20 ( 192.168.31.20 )
6 * * *
8 * * *
10 * * *
9 nsg-static-117.206.71.182.airtel.in ( 182.71.206.117 )
10 182.79.239.197 ( 182.79.239.197 )
11 * * *
13 * * *
15 * * *
17 * * *
19 * * *
21 * * *
23 * * *
25 * * *
27 * * *
20 maa05s24-in-f14.1e100.net ( 142.250.193.110 )
```