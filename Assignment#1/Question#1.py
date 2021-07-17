'''
 *      (Average speed in miles) Assume a runner runs 14 kilometers in 45 minutes and 30 seconds.
 *       Write a program that displays the average speed in miles per hour.
 *      (Note that 1 mile is 1.6 kilometers.)
 '''

kilometers = 14
miles = kilometers / 1.6
rate = (45.0 + 0.5) / (60)   #45 minutes are given while 30 seconds are converted into 0.5minute
milesPerHour = miles / rate
print("speed in miles per hour is: " , milesPerHour)