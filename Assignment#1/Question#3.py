'''
(Science: calculating energy) Write a program that calculates the energy needed
to heat water from an initial temperature to a final temperature. Your program
should prompt the user to enter the amount of water in kilograms and the initial
and final temperatures of the water. The formula to compute the energy is
Q = M * (finalTemperature – initialTemperature) * 4184
where M is the weight of water in kilograms, temperatures are in degrees Celsius,
and energy Q is measured in joules.
'''


initial_Temperature = eval(input("Enter the initial temperature: "))
final_Temperature = eval(input("Enter the final temperature: "))
M_in_kgs = eval(input("Enter weight of water in kilograms: "))
energy = M_in_kgs * (final_Temperature - initial_Temperature) * 4184
print("energy Q is measured in joules is: " , energy)