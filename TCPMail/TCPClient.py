from socket import *
import sys
serverName = sys.argv[1]
serverPort = 2025

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#clientSocket.makefile("w").writelines(sentence+"\n")
modifiedSentence = clientSocket.makefile().readline()
print("FROM SERVER: ", modifiedSentence)
clientSocket.makefile("w").writelines("HELO luigi.monta\n")
modifiedSentence = clientSocket.makefile().readline()
print("FROM SERVER: ", modifiedSentence)
clientSocket.makefile("w").writelines("MAIL FROM: <"+sys.argv[2]+">\n")
modifiedSentence = clientSocket.makefile().readline()
print("FROM SERVER: ", modifiedSentence)
clientSocket.makefile("w").writelines("RCPT TO: <"+sys.argv[3]+">\n")
modifiedSentence = clientSocket.makefile().readline()
print("FROM SERVER: ", modifiedSentence)
clientSocket.makefile("w").writelines("DATA\n")
modifiedSentence = clientSocket.makefile().readline()
print("FROM SERVER: ", modifiedSentence)
dati = input()
clientSocket.makefile("w").writelines(dati+"\n.\n")
modifiedSentence = clientSocket.makefile().readline()
print("FROM SERVER: ", modifiedSentence)
clientSocket.makefile("w").writelines("QUIT\n")
modifiedSentence = clientSocket.makefile().readline()
print("FROM SERVER: ", modifiedSentence)
clientSocket.close()
