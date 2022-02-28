l = list(map(int, input("enter a list of numbers (e.g, 1, 2, 3, 4, 5 (make sure its sorted!)): ").split(',')))
target = int(input("enter a number: "))
lower = 0
upper = len(l)
    
while lower != upper:            
    midpoint = len(list(range(lower, upper))) // 2
    
    if l[lower:][midpoint] == target:
        print(f"Target found at index {midpoint + lower}")
        break
    elif l[lower:][midpoint] < target:
        lower = midpoint + lower
    elif l[lower:][midpoint] > target:
        upper = midpoint + lower

if lower == upper:         
    if l[lower] == target:
        print(f"Target found at index {lower}")
    else:
        print("Target not in list")
