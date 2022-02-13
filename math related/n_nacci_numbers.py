def n_nacci(x, y, z):
    nums = [x]
    for i in range(y-1):
        nums.append(1)

    for i in range(z):
        nums.append(sum(nums[i:y+i]))

    return nums

print(n_nacci(int(input("What number do you want to start with?: ")), int(input("What is the step of the sequence?: ")), int(input("How many numbers do you want to display?: "))))