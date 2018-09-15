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
