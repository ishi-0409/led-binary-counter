import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
led_pins=[29,31,33,35,37]
for pin in led_pins:
        GPIO.setup(pin,GPIO.OUT)

def show_binary(n):
        for i in range(len(led_pins)):
                bit=(n>>i)&1
                GPIO.output(led_pins[i],bit)
try:
        count=0
        while True:
                show_binary(count)
                count=(count+1)%32
                time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()
