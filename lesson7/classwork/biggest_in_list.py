nums= {7,4,1,-4,5,67,0,-1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,-100,-200,-300,-400,-500,-600,-700,-800,-900,-1000}
print(nums)

#you can use built in phython functions to find the biggest and smallest items.
biggest_item = max(nums)
smallest_item = min(nums)

print(" The biggest item",biggest_item)
print(" The smallest item",smallest_item)
    
print("Our algorithm:")

biggest = nums[0]
for i in range(1, len(nums)):
    item = nums[i]
    if item > biggest:
        biggest = item
print("The biggest item is",biggest)
# or if nums[i]>biggest: biggest = nums[i]
