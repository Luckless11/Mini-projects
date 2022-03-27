import random as rand

temp = input("enter a list of numbers (e.g., 5, 2, 3, 1, 4) or leave blank if you want a random unsorted list: ")
nums = list(map(int, temp.split(","))) if bool(len(temp)) else list(range(1, rand.randint(2, 50)))

if not bool(len(temp)):
    rand.shuffle(nums)
    
temp = input("enter 1 if you want to see every state, else, leave blank: ")
states = bool(int(temp)) if temp else False
comps = 0
swaps = 0

print(f"the unsorted list is {nums}\n")

for i in range(len(nums)):
    minimum = i
    for j in range(1 + minimum, len(nums)):
        comps += 1
        if nums[j] < nums[minimum]:
            minimum = j
    if i != minimum:
        nums[i], nums[minimum] = nums[minimum], nums[i]
        swaps += 1
    if states:
        print(nums)

print(f"\nThe sorted list is {nums}, it took {comps} comps and {swaps} swaps to sort the list")