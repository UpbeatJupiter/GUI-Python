import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 4017))

msg = client.recv(1024).decode("utf-8")
print(msg)
client.send(bytes("test message.", "utf-8"))
msg = client.recv(1024).decode("utf-8")
print(msg)
