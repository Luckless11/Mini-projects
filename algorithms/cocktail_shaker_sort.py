def bubble(l, j):
    sorted = False
    if j:
        states = []
    swaps = 0
    comparisons = 0
    temp = 0
    temp2 = 0
    
    while not sorted:
        sorted = True
        for i in range(0 + temp2, len(l)-temp):
            if i != (len(l)-temp)-1:
                if l[i] > l[i+1]:
                    comparisons += 1
                    l[i], l[i+1] = l[i+1], l[i]
                    swaps += 1
                    sorted = False
                    if j:
                        states.append(l.copy())
        temp += 1

        for i in range(len(l)-temp, -1 + temp2, -1):
            if i != 0:
                if l[i] < l[i-1]:
                    comparisons += 1
                    l[i], l[i-1] = l[i-1], l[i]
                    swaps + 1
                    if j:
                        states.append(l.copy())
        temp2 += 1
    
    print(f"Swaps: {swaps} \nComparisons: {comparisons}")

    if j:
        return states
    return l

print(bubble([int(i) for i in input("enter a list of numbers separated by commas (e.g., 5,2,3,1,4): ").split(',')], bool(int(input("enter 1 if you want to see each state, else, enter 0: ")))))