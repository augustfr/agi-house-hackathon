import socket
import time
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connect the client to the server
server_address = ('10.1.8.110', 8080)
client.sendto(b'Starting transmission', ('10.1.8.110', 8080))

# while True:
#     try:
#         reply, address = client.recvfrom(1024)
#         if "<PingPing>" in reply.decode():

#             # send a "pong" response to the server
#             client.sendto(b'Pong', ('10.1.8.109', 8089))

#             # print the response
#             print('Sent: Pong')

#         #print(f'Received from {address}:{reply.decode()}')

#     except socket.timeout:
#         # handle the case where recv() times out
#         print('Timeout occurred, waiting for data...')
#         continue

client.close()