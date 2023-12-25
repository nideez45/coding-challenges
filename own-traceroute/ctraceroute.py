import socket 
import argparse


def main():
    parser = argparse.ArgumentParser(description='Custom traceroute')
    parser.add_argument('domain', metavar='domain', type=str, help='Domain to traceroute for')

    args = parser.parse_args()
    print(args.domain)
    

if __name__ == "__main__":
    main()