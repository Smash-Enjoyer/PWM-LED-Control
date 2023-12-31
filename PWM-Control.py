import board
import analogio as aio
import time
import pwmio as pw

pot = aio.AnalogIn(board.A1)
#how to get a range of 0-1 without including 1(value-min)/(max-min+1)
led = pw.PWMOut(board.LED, frequency=5000, duty_cycle = 0)
#Percent on is going to be the value from the potentiometer turned into a percent brightness.
percent_on = 99
max = 65535
min = 32

def bright():
    percent_on = (pot.value - min)/(max-min+1)
    led.duty_cycle = int(65535 * percent_on / 100)
    time.sleep(0.1)
    print(pot.value)
    time.sleep(0.1)    
    
def dim():
    percent_on = 1 - (pot.value - min)/(max-min+1)
    led.duty_cycle = int(65535 * percent_on / 100)
    time.sleep(0.1)
    print(pot.value)
    time.sleep(0.1)

while True:
    bight()
