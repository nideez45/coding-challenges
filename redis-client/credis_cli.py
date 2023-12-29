import socket 
import argparse
from serializer import *
from deserializer import *
import shlex
"""
    command1  =  *3\r\n$3\r\nSET\r\n$5\r\nvalue\r\n$1\r\n1\r\n
    response1 =  +OK\r\n
    
    command2  =  *2\r\n$4\r\nINCR\r\n$5\r\nvalue\r\n
    response2 =  :2\r\n'
"""

"""
Supported commands
1. PING
2. ECHO <some string>
3. SET <key> <value>
4. GET <key>
5. EXISTS <key>
6. INCR <key>
7. DECR <key>
8. FLUSHALL
"""

class RedisClient:
    def __init__(self, hostname='127.0.0.1', port=6379):
        self.hostname = hostname
        self.port = port
        self.redis_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.redis_socket.connect((hostname, port))

    def _serialize(self, command_string):
        tokens = shlex.split(command_string)
        tokens[0] = tokens[0].lower()
        if tokens[0] not in ["ping", "echo", "set", "get", "exists", "incr", "decr", "flushall"]:
            raise ValueError("Command doesn't exist")

        return Serializer.serialize(tokens)

    def execute_command(self, command):
        serialized_command = self._serialize(command)
        self.redis_socket.send(serialized_command.encode('utf-8'))
        response = self.redis_socket.recv(4096).decode('utf-8')
        response = Deserializer.deserialize(response)
        return response

    def close(self):
        self.redis_socket.close()

def handle_connection(hostname, port):
    redis_client = RedisClient(hostname, port)
    
    while True:
        try:
            print("{}:{}>".format(hostname, port), end='')
            input_command = input()
            
            if input_command == "exit":
                redis_client.close()
                break
            
            response = redis_client.execute_command(input_command)
            if response is None:
                print("(nil)")
            else:
                print(response)
        
        except ValueError as e:
            print("Error", e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Redis Client')
    parser.add_argument('-p', '--port', type=int, default=6379, help='Redis server port')
    parser.add_argument('-H', '--hostname', default='127.0.0.1', help='Redis server hostname')

    args = parser.parse_args()
    handle_connection(args.hostname, args.port)



