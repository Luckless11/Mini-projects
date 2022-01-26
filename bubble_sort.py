def bubble(l, j):
    sorted = False
    if j:
        states = []
    
    while not sorted:
        sorted = True
        for i in range(len(l)):
            if i != len(l)-1:
                if l[i] > l[i+1]:
                    l[i], l[i+1] = l[i+1], l[i]
                    sorted = False
                    if j:
                        states.append(l.copy())
    if j:
        return states
    return l

print(bubble([int(i) for i in input("enter a list of numbers separated by commas (e.g., 5,2,3,1,4): ").split(',')], bool(int(input("enter 1 if you want to see each state, else, enter 0: ")))))