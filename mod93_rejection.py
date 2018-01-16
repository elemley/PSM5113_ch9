from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from random import *


def f(x):
    tmp = 2*pi*sin(4*pi*x)
    return tmp


# test of rejection sampling

n = 300  # number of plot points for function
xstart = 0.0
xend = 0.25
x = [xstart]
dx = (xend - xstart) / n
for i in range(1, n):
    x.append(xstart + i * dx)  # make the x list for the function

upperbound = 2*pi   #have to know this to use this kind of sampling
n_samples = 50000  # number of times to sample from dist.
bins = 32  # number bins to show on hist.
prob = [0]  # gauss_prob is list holding samples from the dist.
for i in range(1, n_samples):
    randInterval = uniform(xstart,xend)  # param of Method
    randUpperBound = uniform(0,upperbound)  # param of Method
    if f(randInterval)>randUpperBound:
        prob.append(randInterval)  # sample from dist.

prob.pop(0)  # get rid of placeholder

title_base = "Sampling by Rejection"
title = title_base
filename = "mod93_rejection_sampling.png"
xlabel = "x"
ylabel = "Probability"

#FunctionPlot111(x, exp1, r, xlabel, ylabel, title, filename)

Function0HistPlot111(x, f, prob, bins, xlabel, ylabel, title, filename)

# Function2Plot111(x,gaussian,mu,sigma,xlabel,ylabel,title,filename)

# HistPlot111(x,bins,xlabel,ylabel,title,filename)

