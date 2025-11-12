#!/usr/bin/env python3
import socket
from datetime import datetime

#import socket importa el módulo estándar de Python que permite trabajar con sockets de red
#from datetime import datetime importa la clase datetime del módulo datetime, usada para obtener la fecha y hora actual del sistema.

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # <-- SOCKET UDP
print("Socket UDP creado")

#socket.AF_INET familia de direcciones IPv4.
#socket.SOCK_DGRAM  tipo de socket UDP
#Se imprime un mensaje informativo para confirmar que el socket se creó correctamente.

servidor.bind(('127.0.0.1', 12345))
print("Servidor escuchando en puerto 12345")

#bind((host, port)) asocia el socket a una dirección IP y puerto específicos
#Se imprime un mensaje de confirmación para confirmar que el servidor esta escuchando en el puerto 12345

while True:

    mensaje, direccion_cliente = servidor.recvfrom(1024)
    print(f"Cliente conectado: {direccion_cliente}")
    
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Enviando: {hora}")
    
    servidor.sendto(hora.encode(), direccion_cliente)

#Espera el mensaje UDP para confirmar que hay un cliente esperando el mensaje de la hora
#Crea el mensaje de hora
#Envia el mensaje de la hora a la dirección del cliente