from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from random import *

def f(x):
    #define f(x) here... this is the curve you want to find area or integral of
    #tmp = log(log(x))
    #tmp = exp(x)/x #exponential integral (can't integrate analytically)
    #tmp = sin(x)/x #Sinc function integral (can't integrate analytically)
    tmp = sin(pow(x,2)) #Fresnel integral (can't integrate analytically)
    #tmp = exp(-pow(x,2)/2) #Error Function or Gaussian integral (can't integrate analytically)
    #tmp = 1/log(x,e) #Logarithmic integral (can't integrate analytically)
    #tmp = sqrt(1-pow(x,4)) #Elliptic integral (can't integrate analytically)
    #tmp = 2.0*sin(x+pi/4)
    #tmp = -6.0+3.2*x
    #tmp = sqrt(pow(cos(x),2)+1)
    return tmp

def gaussian(x,mu,sigma):
    tmp = 1/sqrt(2*pi*sigma)*exp(-pow(x-mu,2)/2/sigma)
    return tmp

#setup ranges for "box" of area to consider for sampling
#x = [1, 3, 5, 7, 3, 3, 3, 1, 5, 5, 7, 6, 6, 6, 4, 4, 4]    #test of histogram function

"""
#test of using random floats
n=10000
x_0 = random()
x = []
for i in range(1,n):
    tmp = random()
    x.append(tmp)

bins = 10
"""
#test of Gaussian/Normal Sampling

#parameters for gaussian dist.
mu = 100
sigma = 10

n = 300 #number of plot points for function
xstart = -5.0
xend = +5.0
x = [xstart]
dx = (xend-xstart)/n
for i in range(1,n):
    x.append(xstart+i*dx)   #make the x list for the function

n_samples=50000   #number of times to sample from dist.
bins = 50       #number bins to show on hist.
gauss_prob = [0]    #gauss_prob is list holding samples from the dist.
for i in range(1,n_samples):
    a = uniform(0,2*pi)     #a param of Box Muller
    tmp = random()          #rand 0-1
    b = sigma*sqrt(-2*log(tmp)) #b param of Box Muller
    gauss_prob.append(b*sin(a)+mu) #sample from dist. (first of two)
    gauss_prob.append(b*cos(a)+mu) #sample from dist. (second of two)

gauss_prob.pop(0)   #get rid of placeholder

#title_base = "Histogram for Uniform Sampling"
title_base = "Gaussian Function and Box_Muller samples"
title = title_base
filename = "mod93_gauss_sampling.png"
xlabel = "x"
ylabel = "Probability"

Function2HistPlot111(x,gaussian,mu,sigma,gauss_prob,bins,xlabel,ylabel,title,filename)

#Function2Plot111(x,gaussian,mu,sigma,xlabel,ylabel,title,filename)

#HistPlot111(x,bins,xlabel,ylabel,title,filename)

