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
%sudo python3 ctraceroute.py twitter.com
Traceroute to twitter.com (104.244.42.193)... max 30 hops
1 _gateway (192.168.43.1) 18.11 ms
2 192.168.29.10 (192.168.29.10) 117.96 ms
3 * * *
4 192.168.31.20 (192.168.31.20) 57.9 ms
5 * * *
6 * * *
7 nsg-static-117.206.71.182.airtel.in (182.71.206.117) 49.6 ms
8 * * *
9 * * *
10 * * *
11 * * *
12 * * *
13 ae1.3115.edge7.London1.level3.net (4.69.166.2) 4700.67 ms
14 * * *
15 104.244.42.193 (104.244.42.193) 3888.68 ms
```

ICMP destination unreacble / time to live exceeded can be used to identify the routers in between
host and the domain
<a href="https://ibb.co/n821T3L"><img src="https://i.ibb.co/wrHQTJz/Screenshot-from-2023-12-25-20-21-42.png" alt="Screenshot-from-2023-12-25-20-21-42" border="0" /></a>
```
UDP messages are sent with increasing time to live value and destination port values starting with 1 and 33434 respectively.
The last 8 bytes contain the udp header information, which can be used to find the destination port number and order the icmp messages.
```