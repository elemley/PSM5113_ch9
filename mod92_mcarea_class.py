from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *

from random import *


def f(x):
    return 3*x+2

a = 1
b = 10
max = 40
n = 20000
hit =0

for i in range(1,n+1):
    randx = uniform(a,b)
    randy = uniform(0,max)
    if randy <= f(randx):
        hit+=1


f = float(hit)/float(n)
area = (b-a)*max*f

print area


