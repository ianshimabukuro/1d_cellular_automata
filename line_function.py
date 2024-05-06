import numpy as np


def line_to_line_function(array):
    next = np.array([])
    j=0
    for i in range(0,array.size):
        if i == 0 or i==array.size:
            dummy = np.append(next,0)
            next = dummy

        else:
            j= 1*array[i-1]+5*array[i]
            if j%2 == 0:
                dummy = np.append(next, 0)
                next = dummy
            else:
                dummy = np.append(next, 1)
                next = dummy

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
