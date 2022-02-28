import socket
import threading
# import subprocess
import time

port = 5000
host = "0.0.0.0"

server = socket.socket()

server.bind((host, port))

server.listen(5)

client = []


def WalkieServer():
    print("accepting connections...")
    conn, addr = server.accept()
    client.append(conn)
    print("connection established")
    t = threading.Thread(target=send, args=(conn, ))
    t.start()
    print("connection established")


def send(fromConnection):
    print(client)
    try:
        print("sending data")
        while True:
            data = fromConnection.recv(4096)
            for cl in client:
                if cl != fromConnection:
                    cl.send(data)
                    print(data)
    except:
        # print("Client Disconnected")



#subprocess.Popen(['python', 'WTClient.py'])
time.sleep(0.5)
WalkieServer()
