from machine import Pin, PWM
import time

# Definisikan pin secara manual
servoPin = 23
trigPin = 5
echoPin = 18
led = Pin(2, Pin.OUT)
# Inisialisasi pin servo
servo = PWM(Pin(servoPin))
servo.freq(50)
servo.duty(0)

# Inisialisasi pin-pi lainnya
trig = Pin(trigPin, Pin.OUT)
echo = Pin(echoPin, Pin.IN)

# Variabel untuk menyimpan data jarak
dist = 0
aver = [0, 0, 0]

def measure():
    led.on()
    trig.off()
    time.sleep_us(5)
    trig.on()
    time.sleep_us(15)
    trig.off()
    
    while echo.value() == 0:
        pass
    pulse_start = time.ticks_us()
    
    while echo.value() == 1:
        pass
    pulse_end = time.ticks_us()
    
    duration = pulse_end - pulse_start
    dist = duration // 2 // 29.1
    return dist

def setup():
    servo.duty(0)
    time.sleep_ms(100)
    servo.deinit()

def loop():
    for i in range(3):
        aver[i] = measure()
        time.sleep_ms(10)
    
    dist = sum(aver) // 3

    if dist < 50:
        servo = PWM(Pin(servoPin))
        servo.freq(50)
        servo.duty(40)
        time.sleep_ms(1)
        servo.duty(0)
        time.sleep_ms(3000)
        servo.duty(75)
        time.sleep_ms(1000)
        servo.deinit()

    print(dist)

setup()
while True:
    loop()
