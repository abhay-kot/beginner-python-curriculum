
numbers = [3, 7, 2, 9, 5]
largest = numbers[0]  # Start with the first number as the largest
for number in numbers:
    if number > largest:
        largest = number
print(f"The largest number is: {largest}")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
search_fruit = "cherry"
if search_fruit in fruits:
    print(f"{search_fruit} is found in the list.")
else:    print(f"{search_fruit} is not found in the list.")

if "fig" in fruits:
    print("Fig is found in the list.")
else:    print("Fig is not found in the list.")
# find if "cherry" is in the list and print its index
if "cherry" in fruits:
    index = fruits.index("cherry")
    print(f"Index of cherry: {index}")
else:    print("Cherry not found")

found = False
index = -1
for i in range(len(fruits)):
    if fruits[i] == "cherry":
        found = True
        index = i
        break

if found == True:
    print(f"Index of cherry: {index}")
else:    print("Cherry not found")