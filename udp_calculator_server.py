import socket

with socket.socket(type=socket.SOCK_DGRAM) as server:
    server_address = ('localhost', 10000)
    server.bind(server_address)
    data, address = server.recvfrom(4096)
    data = data.decode()
    if data[1] == '+':
        eq = int(data[0]) + int(data[2])
    if data[1] == '*':
        eq = int(data[0]) * int(data[2])
    if data[1] == '-':
        eq = int(data[0]) - int(data[2])
    if data[1] == '/':
        eq = int(data[0]) / int(data[2])
    server.sendto(str(eq).encode(),address)