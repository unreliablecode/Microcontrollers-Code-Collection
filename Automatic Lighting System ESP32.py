from machine import Pin
from time import sleep

relay = Pin(5, Pin.OUT) #Relay is an inverter the out is the opposite from the In, heres a relay for controlling High Voltage Bulb
relay1 = Pin(21, Pin.OUT) #Relay is an inverter the out is the opposite from the In, heres a relay for controlling High Voltage Bulb
ldr = Pin(22, Pin.IN) #Light Dependent Resistor Module, A resistor that depending on Light around
pir = Pin(19, Pin.IN) #Passive Infrared Module, to Detect if There's a motion

while True: relay.value(ldr.value() == 1 or 0); relay1.value(pir.value() == ldr.value() and ldr.value() == 1)
  #infinite while loop act the same as void Loop() in Arduino ino code
  #here's we're using lambda expression the value of variable relay return the same as value from ldr variable
  #then the relay1 variable value will follow those variable inside when pir and ldr value are the same 

#Connect relay to GPIO 5
#Connect relay1 to GPIO 21
#Connect ldr to GPIO 22
#Connect pir to GPIO 19
