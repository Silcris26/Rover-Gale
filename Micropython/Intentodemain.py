# import usocket as socket
import socket
from machine import Pin, PWM
import time



# Configura los pines para el L293D
izqin1 = Pin(23, Pin.OUT)
izqin2 = Pin(22, Pin.OUT)
izqvel = PWM(Pin(21), freq=1000, duty=512)  # 50% del ciclo de trabajo
derin1 = Pin(19, Pin.OUT)
derin2 = Pin(18, Pin.OUT)
dervel = PWM(Pin(17), freq=1000, duty=512)  # 50% del ciclo de trabajo

    
# Agregar nport de donde está el servidor TCP, en el ejemplo: 3000
serverAddressPort = socket.getaddrinfo('0.0.0.0', 3000)[0][-1]
# Cantidad de bytes a recibir
bufferSize  = 128

# Descomentar si el esp32 será una estación
#from wifiSTA import connectSTA as connect

# Descomentar si el esp32 estará en modo de acceso AP

from wifiAP import apConfig as connect

# poner acá el nombre de red ssid y password para conectarse
connect("RoverGale","87654321")

# Esta función es de ejemplo,
# Lo que se plantea acá es saber qué hacer con el dato recibido
# En el ejemplo solo se está imprimiendo por terminal
def exec(data):
    print(data)
    if data == b'A':
        izqin1.on()
        izqin2.off()
        derin1.on()
        derin2.off()
        direccion = "hacia adelante"
        
    elif data == b'B':
        izqin1.off()
        izqin2.on()
        derin1.off()
        derin2.on()
        direccion = "hacia atras"
    elif data == b'C':
        direccion ="izquierda"
    elif data == b'D':
        direccion = "derecha"
    elif data == b'E':
        direccion = "detenido"
    else:
        print("Otra opcion")
        direccion = "..." 

    print(f"Motor{direccion}.") 
    time.sleep(2)  # Mantiene el motor encendido por la duración especificada
    apagar_motor()

def apagar_motor():
    print("Apagando el motor...")
    izqin1.off()
    izqin2.off()
    derin1.off()
    derin2.off()



sk = socket.socket()
sk.bind(serverAddressPort)
sk.listen(1)
print("Listening on: ", serverAddressPort)

while True:
    conn, addr = sk.accept()
    while True:
        data = conn.recv(bufferSize)
        # Si dato fue recibido, se decide que hacer con el.
        if data:
            exec(data)
            # Con la siguiente instruccion se pueden enviar datos al
            # dispositivo conectado
            conn.sendall("ok")
            # conn.send("ok")
    conn.close()

