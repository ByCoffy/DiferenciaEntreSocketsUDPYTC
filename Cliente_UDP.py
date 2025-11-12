#!/usr/bin/env python3
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

#socket.socket(...) crea un objeto socket en Python.
#socket.AF_INET indica que usaremos direcciones IPv4.
#socket.SOCK_DGRAM indica que el tipo de socket UDP.

cliente.sendto("".encode(), ('127.0.0.1', 12345))

#sendto(data, addr) envía datos al servidor directamente sin establecer conexión previa (comportamiento típico de UDP).
#''.encode() convierte la cadena vacía '' en bytes usando la codificación por defecto (UTF-8). El código está enviando 
# un mensaje vacío sirve como señal para que el servidor responda.
#('127.0.0.1', 12345) es la tupla (dirección IP, puerto) del destino

print("Solicitud enviada al servidor")

hora, servidor = cliente.recvfrom(1024)
print(f"\nHORA DEL SERVIDOR: {hora.decode()}\n")

#hora.decode() convierte los bytes recibidos a cadena de texto (decodifica con UTF-8 por defecto).
#La f imprime esa cadena en un formato legible: HORA DEL SERVIDOR: <texto recibido>.
#Los \n añaden saltos de línea antes y después para mayor claridad en la salida.

cliente.close()

#cliente.close() cierra el socket y libera recursos.