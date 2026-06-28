# Problem 1
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]
def sum_greater_than_25(nums):
    total = 0
    for i in range(len(nums)):
        item = nums[i]
        if item > 25:
            total += item
    return total
print("The sum of numbers greater than 25 is", sum_greater_than_25(numbers))


# Problem 2
# Find and print the sum of all the numbers less than -10 in the list.
numbers = [-5, -20, -11, 0, 4, -15]
def sum_less_than_negative_10(nums):
    total = 0
    for i in range(len(nums)):
        item = nums[i]
        if item < -10:
            total += item
    return total
print("The sum of numbers less than -10 is", sum_less_than_negative_10(numbers))

# Problem 3
# Find and print the biggest number less than 100 in the list.
numbers = [104, 99, 86, 120, 101]
def biggest_less_than_100(nums):
    biggest = None
    for i in range(len(nums)):
        item = nums[i]
        if item < 100:
            if biggest is None or item > biggest:
                biggest = item
    return biggest
print("The biggest number less than 100 is", biggest_less_than_100(numbers))

# Problem 4
# Find and print the biggest number in the list.
numbers = [12, 7, 33, 5]
def biggest_in_list(nums):
    biggest = nums[0]
    for i in range(1, len(nums)):
        item = nums[i]
        if item > biggest:
            biggest = item
    return biggest
print("The biggest number in the list is", biggest_in_list(numbers))

# Problem 5
# Find and print the total sum of all the numbers in the list.
numbers = [1, 3, 5, 7, 9]
def sum_list(nums):
    total = 0
    for i in range(len(nums)):
        item = nums[i]
        total += item
    return total
print("The sum is", sum_list(numbers))