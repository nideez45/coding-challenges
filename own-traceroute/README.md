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
Traceroute to google.com (142.251.42.14)... max 30 hops
1 _gateway ( 192.168.43.1 )
2 * * *
3 * * *
4 * * *
5 192.168.31.20 ( 192.168.31.20 )
6 * * *
7 * * *
8 * * *
9 nsg-static-117.206.71.182.airtel.in ( 182.71.206.117 )
10 116.119.106.152 ( 116.119.106.152 )
11 * * *
12 * * *
13 * * *
14 * * *
15 * * *
16 * * *
17 * * *
18 * * *
19 * * *
20 bom12s19-in-f14.1e100.net ( 142.251.42.14 )
```