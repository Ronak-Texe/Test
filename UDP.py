import socket
# Is this saving the changes in the repository#
HOST='localhost'
PORT=5454

instance=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
instance.bind((HOST,PORT))

while True:
    msg=instance.recv(40).decode()
    print(msg)
