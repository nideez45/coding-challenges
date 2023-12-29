import socket 
import argparse
from serializer import *
from deserializer import *

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

def serialize(command_string):
    lst = command_string.split(' ')
    lst[0] = lst[0].lower()
    if lst[0] not in ["ping","echo","set","get","exists","incr","decr","flushall"]:
        raise ValueError("Command doesnt exist")
    
    return Serializer.serialize(lst)

def handle_connection(hostname,port):
    redis_socket = socket.socket(family = socket.AF_INET,type= socket.SOCK_STREAM)
    redis_socket.connect((hostname,port))
    
    while True:
        try:
            print("{}:{}>".format(hostname, port), end='')
            input_command = input()
            
            if input_command == "exit":
                redis_socket.close()
                break
            
            serialized_command = serialize(input_command)
            redis_socket.send(serialized_command.encode('utf-8'))
            response = redis_socket.recv(4096).decode('utf-8')
            response = Deserializer.deserialize(response)
            if response == None:
                print("(nil)")
            else:
                print(response)
        
        except ValueError as e:
            print("Error", e)
    
    
def main():
    parser = argparse.ArgumentParser(description='Redis Client')
    
    parser.add_argument('-p', '--port', type=int, default=6379, help='Redis server port')
    parser.add_argument('-H', '--hostname', default='127.0.0.1', help='Redis server hostname')

    args = parser.parse_args()
    hostname = args.hostname 
    port = args.port
    handle_connection(hostname,port)

if __name__ == '__main__':
    main()



