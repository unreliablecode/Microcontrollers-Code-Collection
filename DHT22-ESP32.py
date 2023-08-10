import dht
from machine import Pin
import time
from esp32_gpio_lcd import GpioLcd

lcd = GpioLcd(rs_pin=Pin(5),
                  enable_pin=Pin(17),
                  d4_pin=Pin(18),
                  d5_pin=Pin(19),
                  d6_pin=Pin(21),
                  d7_pin=Pin(22),
                  num_lines=2, num_columns=16)

dht_pin = Pin(4, Pin.IN, Pin.PULL_UP)
dht_sensor = dht.DHT22(dht_pin)

while True:
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        t = "Temp: {:.2f}°C".format(temperature)
        h = "Hum: {:.2f}%".format(humidity)
        res = t + "\n" + h
        lcd.putstr(res)
    except OSError as e:
        print("Error reading DHT sensor:", e)
    time.sleep(2)
    lcd.clear()
