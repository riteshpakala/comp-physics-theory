'''
Program computes gamma(t) for t greater or equal to one. 
If t is an integer, program computes (t-1)! directly.
If t is a float, calculates the integral form of the gamma funciton
>>> abs(abs(gamma(5)) - 24) < 1e-4
True
>>> abs(abs(gamma(4)) - 6) < 1e-4
True
>>> abs(abs(gamma(5./2)) - 1.3293403) < 1e-4
True
>>> abs(abs(gamma(7./2)) - 3.3233509) < 1e-4
True
'''

from math import *
import numpy
import pdb
total = 0
last_total = 0
total_hold = 0
dx = .1
frac = ''

def h(x,t):
    return (x**(t-1))*(e**(-x))

def gamma(t):
    global total
    global last_total
    global total_hold
    if 100 >= t >= 1:
        if type(t) == int:
            return factorial(t-1)
        if type(t) == float:
            global frac
            frac = 'yes'
            total = 0
            for x in numpy.arange (0, 1001):
                total += (dx/6)*(h(x,t) +h(x+dx,t) +4*h((2*x+dx)/2,t))
                if((dx/6)*(h(x,t) +h(x+dx,t) +4*h((2*x+dx)/2,t)) != 0):
                	total_hold = (dx/6)*(h(x,t) +h(x+dx,t) +4*h((2*x+dx)/2,t))
                if(x >= 1000):
                	last_total = total_hold
            return float(total)
    else:
        return 'Please enter a value between 1 and 100.'

def frac_diff():
    if last_total == 0:
        return 'N/A'
    else:
        return abs(total-last_total)/total
   
if __name__ =="__main__":
    t = (7./2)
    import doctest
    doctest.testmod()    
    print 'Gamma of',t,'is:',gamma(t)
    if frac == 'yes':
        print 'frac_diff =', "{:0.7f}".format(frac_diff()*100),"%"