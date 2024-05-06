from line_function import line_to_line_function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import copy
import imageio
line = np.array([0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

bitmap = line

for i in range(0,500):
    new = line_to_line_function(line)
    a=np.vstack((bitmap,new))
    bitmap = a
    line = new
    plt.clf()
    plt.imshow(bitmap, cmap=cm.gray)
    plt.pause(0.1)