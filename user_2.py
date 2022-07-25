# user 2
import socket
port = 1112
address = "127.0.0.1"
BUF_SIZE = 1024
HEADER_SIZE = 10


# creating  object
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((address, port))

# sending data to the server
message = ""
while (message != "exit"):
    message = input("Enter your message: ")
    full_message = "{msg_length:{hs}d}".format(
        msg_length=len(message), hs=HEADER_SIZE) + message
    con.send(bytes(full_message, "utf-8"))

    # receiving data send from the server
    # clearing the message variagle before receiving the respond
    message = ""
    newmsg = True
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
con.close()
