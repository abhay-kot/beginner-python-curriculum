import random

# Problem 1
# Create a list of 4 car brands.
# Print the first and last.
# Then add another brand using append() and print the updated list.
car_brands = ["Toyota", "Honda", "Ford", "Chevrolet"]
print(car_brands[0])  # Print the first car brand
print(car_brands[len(car_brands) - 1])  # Print the last car brand
car_brands.append("Nissan")  # Add another brand using append()
print(car_brands)  # Print the updated list of car brands


# Problem 2
# Create a list of 5 numbers.
# Print the number at index 2.
# Then insert a new number at index 2 and print the updated list.
numbers = [1, 2, 3, 4, 5]
print(numbers[2])  # Print the number at index 2
numbers.insert(2, 10)  # Insert a new number at index 2
print(numbers)  # Print the updated list of numbers


# Problem 3
# Create a list of 3 cities.
# Print the length of the list.
# Then remove one city and print the updated list.
cities = ["New York", "Los Angeles", "Chicago"]
print(len(cities))  # Print the length of the list
cities.remove("Los Angeles")  # Remove one city
print(cities)  # Print the updated list of cities


# Problem 4
# Create a list of 6 file extensions.
# Print a random one.
# Then pop one at index 3 and print the updated list.
file_extensions = [".txt", ".pdf", ".docx", ".xlsx", ".pptx", ".jpg"]
print(random.choice(file_extensions))  # Print a random file extension
file_extensions.pop(3)  # Pop one at index 3
print(file_extensions)  # Print the updated list of file extensions


# Problem 5
# Create a list of 8 names.
# Print the one at the middle index using len().
# Then count how many times a specific name appears.
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"]
middle_index = len(names) // 2  # Calculate the middle index
print(names[middle_index])  # Print the name at the middle index
specific_name = "Alice"
name_count = names.count(specific_name)  # Count how many times the specific name appears
print(name_count)  # Print the count of the specific name   