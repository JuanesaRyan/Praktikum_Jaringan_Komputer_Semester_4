from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(
    ('', serverPort)
)

print("[SYSTEM] Server siap digunakkan")

running = True
while running:
    message, clientAddress = serverSocket.recvfrom(2048)

    decodedMessage = message.decode()

    if decodedMessage.lower() == "exit":
        print("[SYSTEM] Server telah diberhentikan")
        running = False
        continue

    modifiedMessage = decodedMessage.upper()
    print("[SERVER] diterima dari ", clientAddress, " message: ", decodedMessage)

    serverSocket.sendto(
        modifiedMessage.encode(),
        clientAddress
    )

serverSocket.close()
print("[SYSTEM] Socket server telah ditutup")