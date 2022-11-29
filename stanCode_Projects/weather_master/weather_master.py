"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
Exit = -10


def main():
	"""
	Continually ask the user for weather data, until the Exit number is input, then automatically compute the average,
	highest, lowest, cold days among the inputs.
	If the user give the Exit number at first then print "No temperatures were entered".
	"""
	print("stancode\"Weather master 4.0\"!")
	data = int(input("Next Temperature:(or " + str(Exit) + " to quit)? "))
	if data == Exit:
		print('No temperatures were entered.')
	else:
		high = data  # Highest temperature
		low = data  # Lowest temperature
		total = data
		freq = 1  # Frequency
		cold = 0  # cold days
		if data < 16:
			cold += 1
		while True:
			data = int(input("Next Temperature:(or " + str(Exit) + " to quit)? "))
			if data == Exit:
				break
			if data < 16:
				cold += 1
			if high < data:
				high = data
			if low > data:
				low = data
			freq += 1
			total = total + data  # Average
		avg = total / freq
		print('Highest Temperature = ' + str(high))
		print('Lowest temperature = ' + str(low))
		print('Average = ' + str(avg))
		print(str(cold)+' cold day(s)')

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
