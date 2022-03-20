import socket
import sys
from bots import alice, bob, musti, hellokitty
import time


userList = ["alice", "bob", "musti", "hellokitty"]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_address = (sys.argv[1], int(sys.argv[2]))
except Exception as e:
    print("Try again with python .\cli.py localhost 26246")
    exit(1)

try:
    client_socket.connect(client_address)
except Exception as e:
    print("Please start the server first!")


def wait():  # keeps the client connection open
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
            bot(message)
        except:
            client_socket.close()


def bot(data):  # does not work if I put write message instead of data
    if data.startswith("Host: "):
        words = data.split()
        activity = words[14].rstrip("ing")

        if username == userList[0]:
            client_socket.send(alice(activity).encode())
            time.sleep(0.5)  # bør jeg ha for at de skal gå i rekkefølge
        elif username == userList[1]:
            client_socket.send(bob(activity).encode())
            time.sleep(0.5)
        elif username == userList[2]:
            client_socket.send(musti(activity).encode())
            time.sleep(0.5)
        else:
            client_socket.send(hellokitty(activity).encode())
            time.sleep(0.5)


username = input("Choose your username: alice, bob, musti, hellokitty\n")
while username.lower() not in userList:  #  and username.lower() not in usernameList:
    username = input("The username either does not exist or it is already in use!\nPlease write a valid username!\n")

client_socket.send(username.lower().encode())
data = client_socket.recv(1024).decode()  # her får clienten velkommen melding fra server
print(data, username.lower(), "!")

wait()






