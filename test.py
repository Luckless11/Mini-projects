list = list(map(int,input("enter a list of numbers (e.g., 1,2,3,4): ").split(",")))

def average_growth(nums):
    mult_num = []
    for i in range(1, len(nums)):
        x = nums[i-1]
        y = nums[i]

        if x == y:
            mult_num.append(1)
            continue

        while(y):
            x, y = y, x % y
        
        y = nums[i]

        if x > 1 and y / x != 1:
            mult_num.append(y / x)
        else:
            mult_num.append(y / nums[i-1])

    return mult_num

print(average_growth(list))