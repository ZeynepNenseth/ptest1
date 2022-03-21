import socket
import sys
from bots import alice, bob, musti, hellokitty, calimero



userList = ["alice", "bob", "musti", "hellokitty", "calimero"]

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
    client_socket.close()
    quit()


def wait():  # keeps the client connection open
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if message == "The chat room is closing! Have a nice day":
                client_socket.close()
                quit()
            if message == "":
                client_socket.close()
                quit()
            print(message)
            bot(message)
    except:
        exit()



def bot(data):  # does not work if I put write message instead of data
    if data.startswith("Host: "):
        words = data.split()
        activity = words[14].rstrip("ing")
        try:
            activity2 = words[16].rstrip("ing")
        except:
            activity2 = None

        if username == userList[0]:
            client_socket.send(alice(activity, activity2).encode())
        elif username == userList[1]:
            client_socket.send(bob(activity, activity2).encode())
        elif username == userList[2]:
            client_socket.send(musti(activity, activity2).encode())
        elif username == userList[3]:
            client_socket.send(hellokitty(activity, activity2).encode())
        elif username == userList[4]:
            inp = input("What do you want calimero to do?\n")
            client_socket.send(calimero(inp).encode())



username = input("Choose your username: alice, bob, musti, hellokitty, calimero\n")
while username.lower() not in userList:
    username = input("The username either does not exist or it is already in use!\nPlease write a valid username!\n")

client_socket.send(username.lower().encode())
data = client_socket.recv(1024).decode()  # her får clienten velkommen melding fra server
print(data, username.lower(), "!")

wait()






