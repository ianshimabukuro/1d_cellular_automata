import numpy as np


def line_to_line_function(x):
    size = x.size
    y = np.array([0,0])
    iteration = np.array([])
    j=np.array([])

    for i in range(0,size-1):
        if i!=0 or i!=size-1:
            j[i] = x[i-1]+x[i]+5*x[i+1]

    for a in range(0,j.size-1):
        if j[a]%2 == 0:
            iteration[a] = 0
        else:
            iteration[a] = 1
    np.append(y,j)
    return next


initial = np.array([0,0,0,0,0,1,0,1,1,1,0,0,0])
next = line_to_line_function(initial)
print(next)
initial = next
next = line_to_line_function(initial)
print(next)
initial = next
next = line_to_line_function(initial)
print(next)
