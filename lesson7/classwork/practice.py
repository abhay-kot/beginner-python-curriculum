# Problem 1
# Find and print the total sum of all the numbers in the list.
numbers = [4, 11, 22, -6, 3]
def sum_list(nums):
    total = 0
    for i in range(len(nums)):
        item = nums[i]
        total += item
    return total
print("The sum is",sum_list(numbers))

# Problem 2
# Find and print the biggest number in the list.
numbers = [-9, 17, 5, -3, 0]
def biggest_in_list(nums):
    biggest = nums[0]
    for i in range(1, len(nums)):
        item = nums[i]
        if item > biggest:
            biggest = item
    return biggest
print("The biggest number in the list is",biggest_in_list(numbers))

# Problem 3
# Find and print the sum of only the negative numbers in the list (negative means less than 0).
numbers = [2, -1, 8, 10, -7, 6]
def sum_negative(nums):
    total = 0
    for i in range(len(nums)):
        item = nums[i]
        if item < 0:
            total += item
    return total
print("The sum of negative numbers is",sum_negative(numbers))

# Problem 4
# Find and print the sum of only the even numbers in the list. 
numbers = [8, 3, 15, 22, 11, 6]
def sum_even(nums):
    total = 0
    for i in range(len(nums)):
        item = nums[i]
        if item % 2 == 0:
            total += item
    return total
print("The sum of even numbers is",sum_even(numbers))

# Problem 5
# Find and print the biggest number that is negative in the list.
numbers = [-1, -30, -5, 7, 12, -2]
def biggest_negative(nums):
    biggest = None
    for i in range(len(nums)):
        item = nums[i]
        if item < 0:
            if biggest is None or item > biggest:
                biggest = item
    return biggest
print("The biggest negative number is",biggest_negative(numbers))