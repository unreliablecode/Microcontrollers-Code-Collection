from machine import Pin
import time

trigger_pin = Pin(4, Pin.OUT)
echo_pin = Pin(5, Pin.IN)
led_pin = Pin(2, Pin.OUT)
buzzer_pin = Pin(12, Pin.OUT)

def measure_distance():
    trigger_pin.on()
    time.sleep_us(10)
    trigger_pin.off()

    pulse_start = 0
    pulse_end = 0

    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 0.0343 / 2
    return distance

def park_distance_alert(distance):
    if distance < 10:
        led_pin.on()
        buzzer_pin.on()
        time.sleep(0.5)
        led_pin.off()
        buzzer_pin.off()

while True:
    distance = measure_distance()
    park_distance_alert(distance)
    time.sleep(0.1)
