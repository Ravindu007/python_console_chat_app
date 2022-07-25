# echo server
from email import message
import socket
port = 1112
address = "127.0.0.1"
BUF_SIZE = 1024
HEADER_SIZE = 10


# creating object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address, port))
server.listen(5)
print("listenning...")

# run server infinitely
while True:
    # accepting client
    con, addr = server.accept()
    # receiving data from client
    message = ""
    while (message != "exit"):
        message = ""
        newmsg = True
        msg_length = 0
        # loop till the full message receiving
        while True:
            data = con.recv(BUF_SIZE)
            if newmsg:
                msg_length = int(data[:HEADER_SIZE].decode("utf-8"))
                message += data[HEADER_SIZE:].decode("utf-8")
                newmsg = False
            else:
                message += data.decode("utf-8")

            if(len(message) >= msg_length):
                print(message)
                break

        input_message = input("Enter your message: ")
        con.send(bytes("{msg_length:{hs}d}".format(
            msg_length=len(input_message), hs=HEADER_SIZE) + input_message, "utf=8"))

        if(message == "exit"):
            print("Finish conversation")
