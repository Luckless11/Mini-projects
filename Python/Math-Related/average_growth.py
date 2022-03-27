# I originally made this way too complicated by finding the GCF of x and y and dividing y by the GCF unless it's equal to 1, if it's equal
# to 1, then divide y by x, so when I entered 25 and 45 it didn't work

def average_growth(nums):
    mult_num = []
    for i in range(1, len(nums)):
        x = nums[i-1]
        y = nums[i]

        if x == y:
            mult_num.append(1)
            continue

        mult_num.append(y / x)

    return f"The average growth of the list is {sum(mult_num) / len(mult_num)} and growth of each number to get the next is {mult_num}"

print(average_growth(list(map(float, input("enter a list of numbers (e.g., 1, 2, 3, 4): ").split(",")))))