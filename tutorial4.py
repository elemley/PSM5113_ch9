from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *

from random import *

r1=random() #get a
print r1


a = 2
b = 7
r2=randint(a,b)

c = 3.5
d = 46.5
r3 = uniform(c,d)

print r1, r2, r3

r = random()
print r
if r < 0.5:
    print "less than 0.5"

r = random()
print r
if r < 0.5:
    print "less than 0.5"
else:
    print "at least 0.5"

r = random()
print r
if r < 0.25:
    print "first quarter"
elif r < 0.5:
    print "second quarter"
elif r < 0.75:
    print "third quarter"
else:
    print "fourth quarter"

r3 = randint(1,6)
r4 = randint(1,6)

if r3 == r4:
    print "doubles"

if r3==6 and r4 ==6:
    print "A 12!"
else:
    print r3
    print r4

