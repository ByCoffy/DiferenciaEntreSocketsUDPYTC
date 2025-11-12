#!/usr/bin/env python3
import socket
from datetime import datetime

#import socket importa el módulo estándar de Python que permite trabajar con sockets de red (TCP o UDP)
#from datetime import datetime importa la clase datetime del módulo datetime, usada para obtener la fecha y hora actual del sistema

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket TCP creado")

#socket.AF_INET  indica que se usará direcciones IPv4
#socket.SOCK_STREAM indica que el protocolo utilizado será TCP
#Se imprime un mensaje de confirmación indicando que el socket TCP se ha creado correctamente

servidor.bind(('127.0.0.1', 12345))
print("Servidor en puerto 12345")

#bind((host, port)) asocia el socket a una dirección IP y a un puerto específicos
#Se imprime un mensaje para confirmar que el servidor está listo en ese puerto

servidor.listen(5)
print("Esperando clientes...")

#listen(5) pone el socket en modo de escucha, listo para aceptar conexiones TCP entrantes
#El parámetro (5) indica el número máximo de conexiones en espera (cola de clientes)
#Se muestra un mensaje indicando que el servidor está esperando conexiones

while True:
    cliente, direccion = servidor.accept()
    print(f"Cliente conectado: {direccion}")

    #accept() acepta una nueva conexión entrante
    #Devuelve una tupla (cliente, direccion)
    # 'cliente' es un nuevo socket que se usará para comunicarse con ese cliente específico
    # 'direccion' contiene la IP y puerto del cliente
    #Se imprime un mensaje mostrando la dirección del cliente conectado

    mensaje = cliente.recv(1024)

    #recv(1024) recibe hasta 1024 bytes enviados por el cliente
    #En este caso, el cliente puede enviar un mensaje vacío solo para solicitar la hora

    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Enviando: {hora}")

    #datetime.now() obtiene la fecha y hora actuales del sistema
    #Se imprime en consola la hora que se enviará al cliente

    cliente.send(hora.encode())

    #send(data) envía datos al cliente a través de la conexión TCP
    #hora.encode() convierte la cadena de texto en bytes antes de enviarla

    cliente.close()
    print("Conexión cerrada\n")

    #close() cierra la conexión TCP con ese cliente
    #Después de cerrar, el servidor continúa el bucle while para aceptar nuevos clientes