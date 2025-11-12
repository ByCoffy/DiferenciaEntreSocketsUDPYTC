#!/usr/bin/env python3
import socket

#import socket importa el módulo estándar de Python que permite trabajar con sockets de red

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.AF_INET  indica que se usa direcciones IPv4
#socket.SOCK_STREAM indica que se usará el protocolo TCP

cliente.connect(('127.0.0.1', 12345))
print("Conectado al servidor")

#connect((host, port)) establece una conexión con el servidor en la dirección IP y puerto indicados
#Se imprime un mensaje de confirmación indicando que el cliente se conectó correctamente al servidor

cliente.send("".encode())

#send(data) envía datos al servidor a través de la conexión TCP
#"".encode() convierte una cadena vacía en bytes, que es el formato que TCP necesita para enviar información
#En este caso se envía un mensaje vacío para solicitar la hora al servidor

hora = cliente.recv(1024)
print(f"\nHORA DEL SERVIDOR: {hora.decode()}\n")

#recv(1024) recibe hasta 1024 bytes de datos enviados por el servidor
#hora.decode() convierte los bytes en una cadena de texto (UTF-8)
#Se muestra por pantalla la hora enviada por el servidor

cliente.close()

#close() cierra la conexión TCP con el servidor y libera los recursos asociados al socket