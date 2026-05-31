# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
core1 = int(input("Enter your first test score: "))
core2 = int(input("Enter your second test score: "))

if core1 >= 50 and core2 >= 50:
    print("You passed both!")
else:
    print("You failed at least one.")

# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."


lunch = input("Did you bring lunch? (yes/no): ")
water = input("Did you bring water? (yes/no): ")

if lunch == "yes" or water == "yes":
    print("You're somewhat ready.")
if lunch == "yes" and water == "yes":
    print("You're fully ready!")
if lunch == "no" and water == "no":
    print("You're not ready.")


# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
ask = int(input("Enter a number: "))

if ask < 1 or ask > 10:
    print("Out of range.")
else:
    print("In range.")

# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
gess = int(input("Guess a number between 1-10:"))
if(gess == 5 and gess % 2 == 0): 
    print("Even match!")
elif(gess == 5 or gess % 2 == 0):
    print("Nice try!")
else:
    print("Nope.")

# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Boring pair."
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if (num1 % 5 == 0 and num2 % 2 !=0)or (num2 % 5 ==0 and num1 % 2 !=0): 
    print("Interesting pair!")
else:
    print ("Boring pair.")