import socket

# to send objects look into pickle

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # 2048 should match
    print(client.recv(HEADER).decode(FORMAT))


running = True

while running:
    result = input("> Player2: ")
    if result == "q" or result == "quit":
        running = False
    else:
        send(result)
        # send({"message": "player1 test"})

send(DISCONNECT_MESSAGE)
