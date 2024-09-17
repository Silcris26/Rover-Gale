from machine import Pin, PWM
import time

# Configuración del servomotor
servo_pin = Pin(15)  # Pin de control del servomotor
servo = PWM(servo_pin, freq=50)  # Frecuencia de 50 Hz

def set_angulo(angulo):
    # Convertir el ángulo a un ciclo de trabajo
    duty = int((angulo / 180) * 102 + 26) 
    servo.duty(duty)

try:
    while True:
        # Mover el servomotor a 0 grados
        set_angulo(0)
        time.sleep(1)
        
        # Mover el servomotor a 90 grados
        set_angulo(90)
        time.sleep(1)
        
        # Mover el servomotor a 180 grados
        set_angulo(180)
        time.sleep(1)

except KeyboardInterrupt:
    # Detener el servomotor
    servo.duty(0)
    print("Programa terminado")