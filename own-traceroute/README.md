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
1 _gateway ( 192.168.43.1 )
2 192.168.31.20 ( 192.168.31.20 )
3 nsg-static-117.206.71.182.airtel.in ( 182.71.206.117 )
4 182.79.243.201 ( 182.79.243.201 )
5 bom12s19-in-f14.1e100.net ( 142.251.42.14 )
```