import socket
import sys
import threading
import random
import time
from bots import all_actionList

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 26246

try:
    server_address = (sys.argv[1], port)
except IndexError:
    print("Please try again with python .\server.py localhost")
    exit(1)

server_socket.bind(server_address)
print("starter på adresse ", server_address)
server_socket.listen(4)
print("Waiting for connections")

clientList = []
usernameList = []
action = random.choice(all_actionList)


def broadcast(message, sender):
    if type(message) == str:
        message = message.encode()

    for client in clientList:
        if client is not sender and client is not server_socket:
            client.send(message)
    time.sleep(0.2)


def process(sock):
    while True:
        try:
            message = sock.recv(1024)
            broadcast(message)
        except:  # removes clients/username
            index = clientList.index(sock)
            clientList.remove(sock)
            sock.close()
            username2 = usernameList[index]
            broadcast(f"{username2} has left the chat!".encode())
            usernameList.remove(username2)
            break


# starts the chat initiated from the host when all 4 clients are connected
def chat():  # while True:?
    message = "Host: " + action
    print(action)
    #  message = ("Host: Hi everyone! It's a beautiful day. Shall we today?")

    for client in clientList:
        client.send(message.encode())
    for client in clientList:
        message = client.recv(1024)
        time.sleep(0.2)
        broadcast(message, server_socket)


def endAllConnections():
    broadcast("The chat room is closing! Have a nice day", server_socket)
    usernameList.clear()
    clientList.clear()
    time.sleep(0.2)
    server_socket.close()


def handleConnections():
    while len(clientList) < 4:
        while True:
        #try:
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
       # except:


        if len(clientList) == 4:
            print("Start")
            broadcast("Chat room is ready to start!", server_socket)
            time.sleep(0.2)

            try:
                thread = threading.Thread(target=chat)
                thread.start()
                thread.join()

                message = "Thank you for joining the chat today! I think it is best to stick to {action}."
                broadcast(message).encode()
                time.sleep(0.5)
                print("\nBye!.")
                endAllConnections()
            except Exception as e:
                endAllConnections()


handleConnections()
