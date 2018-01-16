from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from random import *

plt.axes()
lst = [1,3,5,7,9,11]


#circle = plt.Circle((0, 0), 0.75, fc='y')
#plt.gca().add_patch(circle)

#rectangle = plt.Rectangle((10,10),100,100,fc='r')
#plt.gca().add_patch(rectangle)

#line = plt.Line2D((2,8),(6,6),lw=2.5)
#plt.gca().add_line(line)

dotted_line = plt.Line2D((2, 8), (4, 4), lw=5.,ls='-.', marker='.', markersize=50, markerfacecolor='r', markeredgecolor='r', alpha=0.5)
plt.gca().add_line(dotted_line)


#points = [[2, 1], [8, 1], [8, 4]]
#polygon = plt.Polygon(points)


plt.axis('scaled')
plt.show()

