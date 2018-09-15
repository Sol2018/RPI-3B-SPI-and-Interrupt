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
<<<<<<< HEAD
=======


def stop(channel):
	global stop_start
	if stop_start:
		print '\nstopping\n'
		stop_start = False
	else:
		print '\nstarting\n'
		stop_start = True
		global counter
		counter = 0 #resetting the last first five values
		global displayResults
		displayResults = [0]*5

def display(channel):
	print("\nFirst Five Results\nTime             Timer           Pot          Temp          Light")

	for x in range(5):
		print displayResults[x]
	print("\n\n")
	
def timerString():
	return '{:02}'.format(int(timer/60)) + ":" + '{:02}'.format(int(timer - 60*(int(timer/60)))) + ":" + '{:02}'.format(int(100*(timer - int(timer))))

def potentiometerValue(channel):
	value = mcp.read_adc(channel)
        volts = (value * 3.3) / float(1024)
	return str(round(volts,1))+" V"

def temperatureValue(channel):
	value = mcp.read_adc(channel)
	volts = (value * 3.3) / float(1024)
	tempC = 100.0*volts - 50.0
	return str(round(tempC,1)) + " C"

def lightValue(channel):
	value = mcp.read_adc(channel)
        volts = (value * 3.3) / float(1024)
        return str(round(100*volts/3.3,1))+" %"

#setting up interrupt hanlders and ignore button for about 200ms after a click has been detected
GPIO.add_event_detect(pins["reset"], GPIO.FALLING, callback=reset, bouncetime=200)
GPIO.add_event_detect(pins["frequency"], GPIO.FALLING, callback=frequency, bouncetime=200)
GPIO.add_event_detect(pins["stop"], GPIO.FALLING, callback=stop, bouncetime=200)
GPIO.add_event_detect(pins["display"], GPIO.FALLING, callback=display, bouncetime=200)



print("Time             Timer           Pot          Temp          Light")
try:
	while True:
		if stop_start:
			global val
			val = str(datetime.now().strftime('%H:%M:%S') +"         "+ timerString() + "        " + potentiometerValue(1)+"        " + temperatureValue(0) +"        "+lightValue(2))
			if counter < 5:
				global counter
				displayResults[counter] = val
				counter = counter + 1
			print val
	       	timer += freq[selector]
        	time.sleep(freq[selector])

except KeyboardInterrupt:
	GPIO.cleanup() # clean up GPIO on CTRL+C exit

#release GPIO pins from their current operations to avoid breaking the RPi
GPIO.cleanup()

>>>>>>> MLSSOL001
