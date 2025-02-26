# Description: Fizz Buzz Program
# Author: Abiodun Magret Oyedele, Lana Starkes and Jeff Woolridge.
# Date(s): Feb 10, 2025 - Feb 10, 2025
 
# Define program constants.
TIMES_TO_EXECUTE = 100

# Perform required calculations.
for i in range(1, TIMES_TO_EXECUTE + 1):

    # Displays "FizzBuzz" when divisible by 5 and 8
    if (i % 5 == 0 and i % 8 == 0):
        print("FizzBuzz")

    # Displays "Fizz" when divisible by 5
    elif (i % 5 == 0):
        print("Fizz")

    # Displays "Buzz" when divisible by 8
    elif (i % 8 == 0):
        print("Buzz")

    # Prints number when none of the criteria is met
    else:
        print(i)
