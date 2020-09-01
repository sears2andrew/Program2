'''
Parking Garage Simulation2 - this program simulates a parking garage of 30 spaces
that has 1-10 cars arriving every 15 minutes for 6 hours, and 0-#arrivals + 2 leaving.
	
this program was written by 
Andrew Sears
Jeff Fakhoury
'''

import random

def getArrivals(open, carsInGarage):
	addedCars = 0
	if open > 10:
		open = 10
	open = open + 1
	if carsInGarage < 30:
		addedCars = random.randrange(1, open)
	return addedCars
	
def getDepartured(addedCars, carsInGarage):
	subtractedCars = random.randint(0, addedCars + 2)
	
	if subtractedCars > carsInGarage:
		subtractedCars = random.randrange(0, carsInGarage)
		
	return subtractedCars

def main():
	carsInGarage = highest = min = hour = 0
	full = False
	
	print ('Parking Garage Simulation \n')
	print ('{:>18}'.format('Cars'), '{:>16}'.format('Cars'), '{:>16}'.format('cars'))
	print ('{:>2}'.format('Time'), '{:>14}'.format('Added'), '{:>18}'.format('Removed'), '{:>18}'.format('Remaining'))
	print ('=' * 57)
	
	while not full:
		addedCars = getArrivals(30 - carsInGarage, carsInGarage)
		subtractedCars = getDepartured(addedCars, carsInGarage + addedCars)
		carsInGarage = carsInGarage + addedCars - subtractedCars
		if carsInGarage > highest:
			highest = carsInGarage
		if carsInGarage < 0:
			carsInGarage = 0
		# find the time for each incriment needed
		if min == 60:
			min = min - 60
			hour = hour + 1
			
		if hour == 5 and min == 45:
			full = True
		# loop all needed variables and print for every change
		print('{0:02}'.format(hour) + ':' + '{0:02}'.format(min), '{:>10}'.format(addedCars), '{:>15}'.format(subtractedCars), '{:>18}'.format(carsInGarage))
		min = min + 15
	print('\nthe highest number of cars in the garage at any given time was', highest)
main()

'''
Parking Garage Simulation

              Cars             Cars             cars
Time          Added            Removed          Remaining
=========================================================
00:00         10               7                  3
00:15          5               3                  5
00:30          6               4                  7
00:45          6               2                 11
01:00          8               6                 13
01:15          9               2                 20
01:30          8               0                 28
01:45          1               1                 28
02:00          2               1                 29
02:15          1               0                 30
02:30          0               0                 30
02:45          0               1                 29
03:00          1               1                 29
03:15          1               0                 30
03:30          0               0                 30
03:45          0               0                 30
04:00          0               0                 30
04:15          0               0                 30
04:30          0               0                 30
04:45          0               1                 29
05:00          1               1                 29
05:15          1               0                 30
05:30          0               0                 30
05:45          0               1                 29

the highest number of cars in the garage at any given time was 30
>>>
Parking Garage Simulation

              Cars             Cars             cars
Time          Added            Removed          Remaining
=========================================================
00:00          5               0                  5
00:15         10               1                 14
00:30          5               3                 16
00:45          4               4                 16
01:00          1               0                 17
01:15          4               3                 18
01:30          4               2                 20
01:45         10               8                 22
02:00          8               4                 26
02:15          3               0                 29
02:30          1               1                 29
02:45          1               2                 28
03:00          2               1                 29
03:15          1               1                 29
03:30          1               1                 29
03:45          1               1                 29
04:00          1               2                 28
04:15          1               0                 29
04:30          1               1                 29
04:45          1               1                 29
05:00          1               2                 28
05:15          2               1                 29
05:30          1               1                 29
05:45          1               1                 29

the highest number of cars in the garage at any given time was 29
>>>
'''

