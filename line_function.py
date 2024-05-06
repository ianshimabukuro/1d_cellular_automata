import numpy as np


def line_to_line_function(x):

    y = np.array([0,0])
    iteration = np.array([])
    for i in range(1,x.size-1):
        #Insert rule, relation between x and y
        if x[i-1]+x[i+1] == 2:
            iteration = np.append(iteration, 1)
        elif x[i-1]+x[i]+x[i+1] == 0:
            iteration = np.append(iteration, 1)
        elif x[i-1]+x[i]+x[i+1] == 3:
            iteration = np.append(iteration, 0)
        else:
            iteration = np.append(iteration, 0)
    y = np.insert(y,1,iteration)
    return y



