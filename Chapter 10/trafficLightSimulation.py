
market_2nd = {'ns' : 'green', 'ew' : 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stopLight):
	for i in range(10):
		for key in stopLight.keys():
			if stopLight[key] == 'green':
				stopLight[key] = 'yellow'
			if stopLight[key] == 'yellow':
				stopLight[key] = 'red'
			if stopLight[key] == 'red':
				stopLight[key] = 'green'
		print(market_2nd)
		print(mission_16th)
		print('\n')

switchLights(market_2nd)
