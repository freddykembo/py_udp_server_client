import socket

client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = "Hi, I am UDP client"

client_sock.sendto(msg.encode("utf-8"),('127.0.0.1',12667))
data,addr = client_sock.recvfrom(2048)
print("Server says:")
print(str(data))

client_sock.close()