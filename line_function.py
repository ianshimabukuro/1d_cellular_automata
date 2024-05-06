import numpy as np


def line_to_line_function(x):

    y = np.array([0,0])
    iteration = np.array([])
    rule = np.array([0,0,0,1,0,1,0,0])
    for i in range(1,x.size-1):
        #Insert rule, relation between x and y
        if x[i-1] == 0 and x[i] == 0 and x[i+1] == 0:
            iteration = np.append(iteration, rule[0])
        elif x[i-1] == 0 and x[i] == 0 and x[i+1] == 1:
            iteration = np.append(iteration, rule[1])
        elif x[i-1] == 0 and x[i] == 1 and x[i+1] == 0:
            iteration = np.append(iteration, rule[2])
        elif x[i-1] == 0 and x[i] == 1 and x[i+1] == 1:
            iteration = np.append(iteration, rule[3])
        elif x[i-1] == 1 and x[i] == 0 and x[i+1] == 0:
            iteration = np.append(iteration, rule[4])
        elif x[i-1] == 1 and x[i] == 0 and x[i+1] == 1:
            iteration = np.append(iteration, rule[5])
        elif x[i-1] == 1 and x[i] == 1 and x[i+1] == 0:
            iteration = np.append(iteration, rule[6])
        elif x[i-1] == 1 and x[i] == 1 and x[i+1] == 1:
            iteration = np.append(iteration, rule[7])
        else:
            iteration = np.append(iteration, 0)
    y = np.insert(y,1,iteration)
    return y



