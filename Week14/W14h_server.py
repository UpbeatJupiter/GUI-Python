import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 4017))
server.listen()

print("Server has been started.")

while True:
    client, address = server.accept()
    print(f"Connection from {address} has been established.")
    client.send(bytes("You have connected to the server.", "utf-8"))
    msg = client.recv(1024).decode("utf-8")
    print(msg)
    client.send(bytes(msg.upper(), "utf-8"))
