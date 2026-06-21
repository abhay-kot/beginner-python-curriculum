# Problem 1
# Count and print how many time "dog" appears in the list.
animals = ["cat", "dog", "cat", "bird", "dog", "cat", "cat", "dog", "cat", "cat"]
print(animals)
print(f"Number of dogs: {animals.count('dog')}")

# Problem 2
# Count and print how many numbers are odd in the list (a number is odd if it's not divisible by 2).
numbers = [13, 22, 8, 19, 6, 7]
odd_count = sum(1 for number in numbers if number % 2 != 0)



# Problem 3
# Search for "monkey" in the list and print its index if it's found.
zoo = ["lion", "elephant", "monkey", "giraffe", "zebra"]  
try:
    index = zoo.index("monkey")
    print(f"Index of monkey: {index}")
except ValueError:
    print("Monkey not found")


# Problem 4
# Search for 99 in the list and print if it’s found.
numbers = [10, 45, 32, 99, 60, 5]
if 99 in numbers:
    print("99 is found in the list.")
else:    print("99 is not found in the list.")


# Problem 4
# Search for 99 in the list and print if it’s found.
numbers = [10, 45, 32, 99, 60, 5]
if 99 in numbers:
    print("99 is found in the list.")
else:    print("99 is not found in the list.")



# Problem 5
# Count and print how many numbers are even in the list (a number is odd if it's divisible by 2).
numbers = [13, 22, 8, 19, 6, 7]
even_count = sum(1 for number in numbers if number % 2 == 0)
print(f"Number of even numbers: {even_count}")