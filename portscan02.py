#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = raw_input("Digite o site ou ip que deseja scannear: ")
portas = input("Digite a quantidades de portas a ser scannear: ")
x = 0
ports = []
while x < portas:
    ports.append(int(raw_input("Digite a porta: ")))
    x += 1

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    conexao = s.connect_ex((host, port))
    if(conexao == 0):
        print (port, "Porta aberta")
    else:
	print(port, "Fechada")
