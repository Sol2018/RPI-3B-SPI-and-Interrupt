import RPi.GPIO as GPIO
import time
import Adafruit_MCP3008
from os import system
from datetime import datetime #current time

#release GPIO pins from their current operations to avoid breaking the RPi
GPIO.setwarnings(False) #supress warning for GPIO cleanup
GPIO.cleanup()

#setting up broadcomm
GPIO.setmode(GPIO.BCM)

#GPIO pins used in this practical
pins = {"reset": 26,
    "frequency": 19,
    "stop": 13,
    "display": 6,
    "CLK": 17,
    "MISO": 4,
    "MOSI": 3,
    "CS": 2}

#setting up the reset, frequency, stop and display button pins to input and their respective pull up/down resistor
GPIO.setup(pins["reset"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pins["frequency"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pins["stop"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pins["display"], GPIO.IN, pull_up_down=GPIO.PUD_UP)

#setting up mcp using Adafruit_MCP3008 library
mcp = Adafruit_MCP3008.MCP3008(clk=pins["CLK"],miso=pins["MISO"], cs=pins["CS"],mosi=pins["MOSI"])

#global variables
timer = 0
freq = [0.5, 1, 2]
selector = 0;
stop_start = True
displayResults = [0]*5
counter = 0

#functions used by buttons
def reset(channel):
    global timer
    timer = 0 #resetting timer value to zero
    system('clear')
    print("Time             Timer           Pot          Temp          Light")

def frequency(channel):
    global selector
    print("\nfrequency changed from "+str(freq[selector]) + "s")
    selector = (selector + 1)%3        #switching current frequency to the next possible frequency in the freq array
    print("to " + str(freq[selector]) + "s\n")
