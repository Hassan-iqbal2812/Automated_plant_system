import time
import datetime
import RPi.GPIO as GPIO
import itertools
motor = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor,GPIO.OUT)
print("Setup Complete")


def main():
	print("Running python script")
	global_time = datetime.datetime.now()
	get_time(global_time)
	print("Finished running script")

def turning_motor_on(motor):
	GPIO.output(motor,GPIO.LOW)
	print("TURNING GPIO.LOW")
	time.sleep(2)
	GPIO.output(motor,GPIO.HIGH)
	print("TURNING GPIO.HIGH")

def comparing_time(glob_time,curr_time):
	print(str(curr_time))
	glob_time_list = [glob_time.year,glob_time.month,glob_time.day,glob_time.hour]
	curr_time_list = [curr_time.year,curr_time.month,curr_time.day,curr_time.hour]
	i = 0
	for glob,curr in itertools.izip(glob_time_list,curr_time_list):
		i+=1
		print("{} : global_time {} curr_time {}".format(i,glob,curr))
		if i is len(glob_time_list):
			if glob == 23 :
				print("Current time is {}".format(curr))
				if curr == 00 :
					print("We need to update")
					return True
				else :
					print("No need we are on the 23rd hour")
			if curr > glob :
				print("Comparing last element")
				print("update glob time")
				print(str(glob_time))
				return True
		else:
			if glob >= curr:
				print("Not last element")
	return False

def get_time(global_time):
	print("Trying to get the current time")
	while(True):
		current_time = datetime.datetime.now()
		time.sleep(5)
		if(comparing_time(global_time,current_time) == False):
			print("Comparing time is false dont turn motor")
		else:
			turning_motor_on(motor)
			global_time = datetime.datetime.now()

if __name__ == "__main__":
	main()
