import time
from machine import Pin, SoftI2C
from onewire import OneWire
from ds18x20 import DS18X20
import ssd1306
from time import sleep

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
pin_dq = Pin(4)
ow = OneWire(pin_dq)
ds18 = DS18X20(ow)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def read_temperature():
    roms = ds18.scan()
    if not roms:
        print("No DS18B20 devices found!")
        return None
    
    ds18.convert_temp()
    time.sleep_ms(750)
    temperature = ds18.read_temp(roms[0])
    return temperature

while True:
    try:
        water_temperature = read_temperature()
        if water_temperature is not None:
            strtemp = "Water Temperature: "
            oled.text(strtemp, 0, 0)
            temp2 = "{:.2f} Celcius".format(water_temperature)
            oled.text(temp2, 0, 10)
            oled.show()
        else:
            print("Failed to read water temperature.")
    except Exception as e:
        print("Error:", e)
    time.sleep(2)
    oled.fill(0) 
