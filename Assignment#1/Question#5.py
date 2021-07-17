'''
Given an airplane’s acceleration a and take-off
speed v, you can compute the minimum runway length needed for an airplane to
take off using the following formula:
length = v**2/2*a or (length = (speed * speed) / (2 * acceleration))
Write a program that prompts the user to enter v in meters/second (m/s) and the
acceleration a in meters/second squared (m/s2), and displays the minimum runway
length.
 '''

speed,acceleration = eval(input("Enter speed and acceleration: "))
length = (speed * speed) / (2 * acceleration)
print("The minimum runway length for this airplane is : ", length , "meters")