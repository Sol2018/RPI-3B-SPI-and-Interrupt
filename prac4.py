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
