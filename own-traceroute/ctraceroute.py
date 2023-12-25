import socket 
import argparse
import threading
import time

Time = {}
ans = {}

def reverse_dns_lookup(ip_address):
    try:
        hostnames, _, _ = socket.gethostbyaddr(ip_address)
        # print(ip_address,hostnames)
        return hostnames
    except socket.herror as e:
        return ip_address


def receive_icmp(domain,ipv4_address):
    print("Traceroute to {} ({})... max 30 hops".format(domain,ipv4_address))
    
    icmp_socket = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    icmp_socket.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
    icmp_socket.settimeout(3)
    while True:
        try:
            rec_packet, addr = icmp_socket.recvfrom(4096)
        except socket.timeout:
            break
        addr = addr[0]
        src_port = int.from_bytes(rec_packet[-6:-4], byteorder='big')
        if src_port<33434 or src_port>33464:
            continue
        ans[src_port] = f"{reverse_dns_lookup(addr)} ({addr}) {round((time.time() - Time[src_port]) * 1000, 2)} ms"
    
 
def send_udp(domain):
    dst_port = 33434
    ttl = 1
    for i in range(30):
        client_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)
        client_socket.sendto("".encode(),(domain,dst_port))
        Time[dst_port] = time.time()
        dst_port+=1
        ttl+=1
    
def print_result(ipv4_address):
    lst = []
    for key,value in ans.items():
        lst.append((key-33434+1,value))
    lst = sorted(lst)
    hop = 1
    for a,b in lst:
        if a == hop:
            print(hop,b)
        else:
            while hop<a:
                print(hop,"* * *")
                hop+=1
            print(hop,b)
        hop+=1
        if ipv4_address in b:
            break
    
def main():
    parser = argparse.ArgumentParser(description='Custom traceroute')
    parser.add_argument('domain', metavar='domain', type=str, help='Domain to traceroute for')

    args = parser.parse_args()
    domain = args.domain
    ipv4_address = socket.gethostbyname(domain)
    udp_thread = threading.Thread(target=send_udp,args=(ipv4_address,))
    icmp_thread = threading.Thread(target=receive_icmp,args=(domain,ipv4_address,))
    udp_thread.start()
    icmp_thread.start()
    time.sleep(5)
    result_thread = threading.Thread(target=print_result,args=(ipv4_address,))
    result_thread.start()
    result_thread.join()
    udp_thread.join()
    icmp_thread.join()
    
if __name__ == "__main__":
    main()