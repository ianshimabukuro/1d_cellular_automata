import numpy as np


def line_to_line_function(x):
    print("Input size:",x.size)
    y = np.array([0,0])
    iteration = np.array([])
    j=np.array([])

    for i in range(1,x.size-1):
        print(i)
        j = np.append(j,x[i-1]+x[i]+5*x[i+1])

    print("Middle size:",j.size)
    for a in range(0,j.size):
        if j[a]%2 == 0:
            iteration = np.append(iteration,0)
        else:
            iteration = np.append(iteration,1)
    print("Middle after bin:",iteration.size)

    y = np.insert(y,1,iteration)

    print("output size:",y.size)
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
