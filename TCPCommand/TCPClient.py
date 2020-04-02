from socket import *
serverName = 'localhost'
serverPort = 6789
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
stringa = input()
clientSocket.makefile("w").writelines(stringa + "\n")
modifiedSentence = clientSocket.makefile().readlines()
for s in modifiedSentence:
    if not s == "<eof>\n":
        print("FROM SERVER: " + s)
clientSocket.close()
