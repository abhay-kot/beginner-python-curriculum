# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
ask = int(input("Enter a number: "))
if ask % 2 == 0:
    print("Even")
else:    print("Odd")   


# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
day = input("Enter the day of the week (all lowercase): ")
if day == "saturday" or day == "sunday":
    print("Weekend")
else:    print("Weekday")   


# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!"
import random
random_number = random.randint(1, 10)       


# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
positive_integer = int(input("Enter a positive integer: "))
if positive_integer > 10 and positive_integer % 2 == 0:
    print("Big even number")
else:    print("Number does not meet criteria")


# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2: 
    print(f"{num1} is larger.")
elif num2 > num1:
    print(f"{num2} is larger.")
else:    print("Numbers are equal.")