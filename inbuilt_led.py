import machine
import time

l = machine.Pin("LED",machine.Pin.OUT)

while True:
    l.off()
    time.sleep(0.2)
    l.on()
    time.sleep(0.5)