nums = [-50,50,0,-15]
print(nums)

total = sum(nums)
print("The sum is",total)

print("Our algorithm:")
#("1. Initialize a variable to store the sum.")
#("2. Iterate through the list.")
#("3. Add each number to the sum.")
#("4. Return the sum.")

total = 0
for i in range(len(nums)):# Go trough the list
    item = nums[i]
    total += item
print("The sum is",total)

total = 0
for i in range(len(nums)):# Go trough the list
    item = nums[i]
    if item >= 0:
        total = total + item
print("The sum of positive numbers is",total)