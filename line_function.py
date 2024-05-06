import numpy as np


def line_to_line_function(x):

    y = np.array([0,0])
    iteration = np.array([])
    print(x.size)
    for i in range(1,x.size-1):
        if x[i-1] == 1:
            iteration = np.append(iteration, 1)
        else:
            iteration = np.append(iteration, 0)

    print(iteration.size)
    y = np.insert(y,1,iteration)
    return y


initial = np.array([0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,0,0,1])
next = line_to_line_function(initial)
print(next)
initial = next
next = line_to_line_function(initial)
print(next)
initial = next
next = line_to_line_function(initial)
print(next)
