'''

HW03
Ritesh Pakala
Partner: Ian Cone

This function finds all prime numbers between 2 given integers. 
Given integers are entered via command line, and then all prime
numbers in between are printed

'''
import numpy as np

def primer(a, b):
    global count;
    for i in range(a, b):
        count = 0
        for j in range(1, i+1):
            if(i%j==0):
                count+=1
        if(count<=2 & i != 1):
            print i
        
primer(1, 101)