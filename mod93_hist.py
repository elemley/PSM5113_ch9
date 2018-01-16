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

#setup ranges for "box" of area to consider for sampling
#x = [1, 3, 5, 7, 3, 3, 3, 1, 5, 5, 7, 6, 6, 6, 4, 4, 4]    #test of histogram function

#test of using random floats
n=10000
x_0 = random()
x = []
for i in range(1,n):
    tmp = random()
    x.append(tmp)

bins = 25


title_base = "Histogram for Uniform Sampling"
title = title_base
filename = "mod93_uniform_sampling.png"
xlabel = "x"
ylabel = "Probability"

HistPlot111(x,bins,xlabel,ylabel,title,filename)


#Function2HistPlot111(x,gaussian,mu,sigma,gauss_prob,bins,xlabel,ylabel,title,filename)

#Function2Plot111(x,gaussian,mu,sigma,xlabel,ylabel,title,filename)



