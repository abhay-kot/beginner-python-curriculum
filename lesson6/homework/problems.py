# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
print(f"Number of times 'Alex' appears: {names.count('Alex')}")



# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
if "elephant" in animals:
    print("Elephant is found in the list.")
else:    print("Elephant is not found in the list.")



# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
print(f"Number of scores that are 100: {scores.count(100)}")



# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
try:
    index = colors.index("blue")
    print(f"Index of blue: {index}")
except ValueError:
    print("Blue not found")



# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]
below_zero_count = sum(1 for temp in temperatures if temp < 0)
print(f"Number of temperatures below zero: {below_zero_count}")