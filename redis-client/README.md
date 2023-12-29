# Write Your Own Redis CLI Tool
Usage
```
usage: credis_cli.py [-h] [-p PORT] [-H HOSTNAME]

Redis Client

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Redis server port
  -H HOSTNAME, --hostname HOSTNAME
                        Redis server hostname
```
Example
```
%  python3 credis_cli.py 
127.0.0.1:6379>ping
PONG
127.0.0.1:6379>echo "hello"
"hello"
127.0.0.1:6379>set value 1
OK
127.0.0.1:6379>get value
1
127.0.0.1:6379>incr value
(integer) 2
127.0.0.1:6379>get value
2
127.0.0.1:6379>exit
```