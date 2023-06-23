import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = ("10.0.0.167",5000)
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

while True:
    DATA = client.recv(2048).decode(FORMAT)
    if not DATA: break
    print("GOT: %s" %DATA)

    MSG = input("MSG: ")

    if not MSG == "break": send(MSG)
    else: break

send(DISCONNECT_MESSAGE)