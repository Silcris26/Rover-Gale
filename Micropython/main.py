# import usocket as socket
import socket
from machine import Pin, PWM
import time



# Configura los pines 
izqin1 = Pin(17, Pin.OUT)
izqin2 = Pin(23, Pin.OUT)
izqvel = PWM(Pin(19), freq=1000, duty=512)  # 50% del ciclo de trabajo
derin1 = Pin(21, Pin.OUT)
derin2 = Pin(16, Pin.OUT)
dervel = PWM(Pin(22), freq=1000, duty=512)  # 50% del ciclo de trabajo
servo_pin = Pin(15)
servo = PWM(servo_pin, freq=50)

    
# Agregar nport de donde está el servidor TCP, en el ejemplo: 3000
serverAddressPort = socket.getaddrinfo('0.0.0.0', 3000)[0][-1]
# Cantidad de bytes a recibir
bufferSize  = 128

# Descomentar si el esp32 será una estación
#from wifiSTA import connectSTA as connect

# Descomentar si el esp32 estará en modo de acceso AP
from wifiAP1 import apConfig as connect

# poner acá el nombre de red ssid y password para conectarse
connect("RoverGale","87654321",3)

# Función 
def exec(data):
    print(data)
    if data == b'A':
        izqin1.on()
        izqin2.off()
        derin1.on()
        derin2.off()
        print("Adelante")
    elif data == b'T':
        izqvel.duty(1023)
        dervel.duty(1023)
        print("Turbo")
    elif data == b'ST':
        izqvel.duty(512)
        dervel.duty(512)
        print("Detener turbo")
    elif data == b'B':
        izqin1.off()
        izqin2.on()
        derin1.off()
        derin2.on()
        print("Atras")
    elif data == b'C':
        mover_servo(60)
        print("Izquierda")
    elif data == b'C1':
        mover_servo(45)
        print("Mas a la izquierda")
    elif data == b'D':
        mover_servo(120)
        print("Derecha")
    elif data == b'D1':
        mover_servo(135)
        print("Mas a la derecha")
    elif data == b'S': 
        izqin1.off()
        izqin2.off()
        derin1.off()
        derin2.off()
        print("Detener")
    elif data == b'E':
        mover_servo(90)
        print("Llantas centradas")
    else:
        print("Otra opcion")
        
def mover_servo(angulo):
    # Convierte el ángulo a un ciclo de trabajo PWM
    # 0° -> 2.5% (40) y 180° -> 12.5% (120)
    duty = int(40 + (angulo / 180) * 80)  # Mapea el ángulo a duty
    servo.duty(duty)
    
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
            #conn.send("ok")
    conn.close()

