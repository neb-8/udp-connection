import socket
import sys

with socket.socket(type=socket.SOCK_DGRAM) as client:
    server_address = ('localhost',10000)
    client.sendto(sys.argv[1].encode(),server_address)
    data, address = client.recvfrom(4096)
    print(data.decode())