def bubble(l, j):
    sorted = False
    if j:
        states = []
    temp = 0
    swaps = 0
    comparisons= 0
    while not sorted:
        sorted = True
        for i in range(len(l)-temp):
            if i != (len(l)-temp)-1:
                if l[i] > l[i+1]:
                    comparisons += 1
                    l[i], l[i+1] = l[i+1], l[i]
                    swaps += 1
                    sorted = False
                    if j:
                        states.append(l.copy())
        temp += 1
    
    print(f"Swaps: {swaps} \nComparisons: {comparisons}")
    if j:
        return states
    return l

print(bubble(list(map(int, input("enter a list of numbers (e.g., 5, 2, 3, 1, 4): ").split(","))), int(input("enter 1 if you want to see each state, else, enter 0: "))))