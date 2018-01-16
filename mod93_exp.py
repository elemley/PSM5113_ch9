from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from random import *

def exp1(x,r):
    tmp = abs(r)*exp(r*x)
    return tmp

#test of exponential sampling
r = -2.0

n = 300 #number of plot points for function
xstart = 0.0
xend = 3.0
x = [xstart]
dx = (xend-xstart)/n
for i in range(1,n):
    x.append(xstart+i*dx)   #make the x list for the function

n_samples=1000   #number of times to sample from dist.
bins = 32       #number bins to show on hist.
exp_prob = [0]    #gauss_prob is list holding samples from the dist.
for i in range(1,n_samples):
    tmp =random()   #param of Exp. Method
    exp_prob.append(log(tmp)/r) #sample from dist.


exp_prob.pop(0)   #get rid of placeholder

title_base = "Exponential Function and Sampling"
title = title_base
filename = "mod93_exp_sampling.png"
xlabel = "x"
ylabel = "Probability"


FunctionHistPlot111(x,exp1,r,exp_prob,bins,xlabel,ylabel,title,filename)

#Function2Plot111(x,gaussian,mu,sigma,xlabel,ylabel,title,filename)

#HistPlot111(x,bins,xlabel,ylabel,title,filename)

