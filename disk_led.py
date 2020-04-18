#!/usr/bin/env python
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from time import sleep  # Import the sleep function from the time module
import os
import psutil


GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)  # Set pin 27 to be an output pin and set initial value to low (off)

disk = psutil.disk_usage("/media/ubuntu/demo/")
#disk_percent_used = disk.percent


try:
        while True:  # Run forever
                path_exists = os.path.exists("/media/ubuntu/demo/")
                disk_percent_used = disk.percent
                #print(disk_percent_used)
                if disk_percent_used > 98 and path_exists == 1:
                                GPIO.output(27, GPIO.HIGH)  # Turn on
                                sleep(1)  # Sleep for 1 second
                                GPIO.output(27, GPIO.LOW)  # Turn off
                                sleep(1)  # Sleep for 1 second
                elif disk_percent_used > 85 and path_exists == 1:
                                GPIO.output(27, GPIO.HIGH)  # Turn on
                else:
                                GPIO.output(27, GPIO.LOW)  # Turn off
                if path_exists == 0:
                                GPIO.output(27, GPIO.HIGH)  # Turn off
                                sleep(1)  # Sleep for 1 second
                                GPIO.output(27, GPIO.LOW)  # Turn off
                                sleep(1)  # Sleep for 1 second                 
                time.sleep(30) # wait to loop again so we don’t use the processor too much.
                
                
except KeyboardInterrupt:
        GPIO.output(27, GPIO.LOW)
        print ('interrupted')


