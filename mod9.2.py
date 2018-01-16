from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from random import *

def f(x):
    #define f(x) here... this is the curve you want to find area or integral of
    tmp = sqrt(pow(cos(x),2)+1)
    #tmp = 3*x+2
    #tmp = log(log(x))
    #tmp = exp(x)/x #exponential integral (can't integrate analytically)
    #tmp = sin(x)/x #Sinc function integral (can't integrate analytically)
    #tmp = sin(pow(x,2)) #Fresnel integral (can't integrate analytically)
    #tmp = exp(-pow(x,2)/2) #Error Function or Gaussian integral (can't integrate analytically)
    #tmp = 1/log(x,e) #Logarithmic integral (can't integrate analytically)
    #tmp = sqrt(1-pow(x,4)) #Elliptic integral (can't integrate analytically)
    #tmp = 2.0*sin(x+pi/4)
    #tmp = -6.0+3.2*x
    #tmp = sqrt(pow(cos(x),2)+1)
    return tmp

def mc_area(f1,xmin,xmax, ymin,ymax):
    n = 1000   #num of MC points to use to determine area
    countplus = 0 #counts a "hit" that is above x-axis
    countminus = 0 # counts a "hit" that is below the x-axis
    x = [xmin]  #setup list for x points that hit (this is returned, but only needed for plotting
    y = [ymin]  #setup list for y points that hit (this is returned, but only needed for plotting
    for i in range(1,n):
        randx = uniform(xmin,xmax)  #gen rand float between xmin and xmax
        randy = uniform(ymin,ymax)  #gen rand float between ymin and ymax
        if f1(randx) > 0:   #is function > 0
            if randy < f1(randx) and randy > 0: #is random pair randx and randy below f but above x-axis?
                countplus +=1   # it's a hit!
                x.append(randx)
                y.append(randy)
        else:               #f(randx) is below x-axis
            if randy > f1(randx) and randy < 0: #is random pair randx and randy above f but below x-axis?
                countminus +=1  #it's a hit!
                x.append(randx)
                y.append(randy)

    plus_fraction = float(countplus)/float(n) #what fraction of MC trials were between x-axis and f(x)>0
    minus_fraction = float(countminus)/float(n) #what fraction of MC trials were between x-axis and f(x)<0
    pos_area = float((ymax-ymin)*(xmax-xmin)*plus_fraction) #calc total area above x-axis
    neg_area = float((ymax-ymin)*(xmax-xmin)*minus_fraction) #calc total area below x-axis
    x.pop(0)    #note, need to remove first list item... it was just a placeholder
    y.pop(0)

    return pos_area, neg_area, x, y

#setup ranges for "box" of area to consider for sampling
xmin = 0
xmax = 2
ymin = 0.0
ymax = 3.0

pos_area, neg_area, x, y = mc_area(f,xmin,xmax,ymin,ymax)   # get vals from mc_area function

print pos_area, neg_area

function_name = "3x+2"
title_base = "Plot of " + function_name
title = title_base
filename = "mod92_"+function_name+".png"
xlabel = "x"
ylabel = "Monte Carlo Points"
y_func_label = function_name


FunctionScatterPlot111(x,xlabel,f,y_func_label,y,ylabel,title,filename)


