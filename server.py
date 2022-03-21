import socket
import sys
import threading
import random
import time
from bots import all_actionList, extra_actionList

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 26246

try:
    server_address = (sys.argv[1], port)
except IndexError:
    print("Please try again with python .\server.py localhost")
    exit(1)

server_socket.bind(server_address)
print("starter på adresse ", server_address)
server_socket.listen()
print("Waiting for connections")

clientList = []
usernameList = []
additional = random.choice([True, False])
action1 = random.choice(all_actionList)
action2 = None
if additional is True:
    while action2 == action1:
        action2 = random.choice(extra_actionList)


def broadcast(message, sender):
    if type(message) == str:
        message = message.encode()

    for client in clientList:
        if client is not sender and client is not server_socket:
            client.send(message)
    time.sleep(0.2)


# starts the chat initiated from the host when all 4 clients are connected
def chat():  # hva med 2 aktiviteter
    if action2 is not None:
        message = "Host: Hi everyone! It's a beautiful day. Would you like to join me for " + action1 + "ing or " \
                  + action2 + "ing today?"
    else:
        message = "Host: Hi everyone! It's a beautiful day. Would you like to join me for " + action1 + "ing today?"
    print(message)

    for client in clientList:
        client.send(message.encode())
    for client in clientList:
        message = client.recv(1024)
        time.sleep(1)
        broadcast(message, server_socket)


def endAllConnections():
    broadcast("The chat room is closing! Have a nice day", server_socket)
    usernameList.clear()
    clientList.clear()
    server_socket.close()
    time.sleep(3)
    quit()


def handleConnections():
    while len(clientList) < 5:
        while True:
            client_socket, client_address = server_socket.accept()
            print("Client connected:", {str(client_address)})
            username = client_socket.recv(1024).decode()

            if username not in usernameList:
                print("Server has received the username", username, "from the client")
                client_socket.send("Welcome to the chat room".encode())
                print(username, "with the connection ", client_socket, "is added to the client list.")
                usernameList.append(username)
                clientList.append(client_socket)
                print(usernameList)
                break
            else:
                client_socket.send("Please choose another username: ".encode())
                print("server fikk username ", username, "fra client")
                client_socket.close()


        if len(clientList) == 5: # husk å endre tilbake til 4
            print("Opening the chat room")
            broadcast("Chat room is ready to start!", server_socket)
            time.sleep(0.2)

            try:
                thread = threading.Thread(target=chat)
                thread.start()
                thread.join()

                message = "Thank you for joining the chat today! I think it is best to stick to " + action1 + "ing."
                broadcast(message, server_socket)
                print(message)
                time.sleep(0.5)
                print("\nBye!")
                broadcast("\nBye!", server_socket)
                endAllConnections()
            except Exception as e:
                print(e)


handleConnections()
