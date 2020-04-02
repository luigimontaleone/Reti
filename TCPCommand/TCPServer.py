from socket import *
import os
serverPort = 6789

welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.bind(('', serverPort))
welcomeSocket.listen(5)
os.chdir("/home/luigi/Scaricati")
while 1:
    connectionSocket, addr = welcomeSocket.accept()
    clientSentence = connectionSocket.makefile().readline()
    if (clientSentence.lower()) == "ls\n":
        currentFolder = os.getcwd()
        listFile = os.listdir(currentFolder)
        for f in listFile:
            connectionSocket.makefile("w").writelines(f)
        connectionSocket.makefile("w").writelines("<eof>\n")
    elif clientSentence.lower().startswith("cat"):
        if os.path.exists(clientSentence[3:-1].strip()) or os.path.isdir(clientSentence[3:-1].strip()):
            file = open(clientSentence[3:-1].strip(), "r")
            for line in file:
                print(line)
                connectionSocket.makefile("w").writelines(line)
            connectionSocket.makefile("w").writelines("<eof>\n")
    elif clientSentence.lower().startswith("cd"):
        if os.path.exists(clientSentence[2:-1].strip()) or os.path.isdir(clientSentence[2:-1].strip()):
            os.chdir(clientSentence[2:-1].strip())
        connectionSocket.makefile("w").writelines(os.getcwd() + "\n")
        connectionSocket.makefile("w").writelines("<eof>\n")
    connectionSocket.close()
