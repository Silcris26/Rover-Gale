from machine import Pin
import time

# Definimos los pines de control del puente H
motor1_in1 = Pin(17, Pin.OUT)  # Control Motor 1
motor1_in2 = Pin(23, Pin.OUT)  # Control Motor 1
motor2_in1 = Pin(21, Pin.OUT)  # Control Motor 2
motor2_in2 = Pin(16, Pin.OUT)  # Control Motor 2

def motor1_adelante():
    motor1_in1.value(1)
    motor1_in2.value(0)

def motor1_atras():
    motor1_in1.value(0)
    motor1_in2.value(1)

def motor2_adelante():
    motor2_in1.value(1)
    motor2_in2.value(0)

def motor2_atras():
    motor2_in1.value(0)
    motor2_in2.value(1)

def detener_motores():
    motor1_in1.value(0)
    motor1_in2.value(0)
    motor2_in1.value(0)
    motor2_in2.value(0)

while True:
    motor1_adelante()
    motor2_adelante()
    time.sleep(2)  # Ambos motores hacia adelante
    
    detener_motores()
    time.sleep(2)  # Parar

    motor1_adelante()
    motor2_atras()
    time.sleep(2)  # Ambos motores hacia atrás
    
    detener_motores()
    time.sleep(2)  # Parar