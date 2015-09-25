#%matplotlib 
import numpy as np
'''

HW03
Ritesh Pakala
Partner: Ian Cone

This function models the wavefunction of two fermions of 
opposite spin and then plots the wavefunction and probablility 
density. x1 and x2 are inputted by the user at the command prompt

   
Call signature  :

    python plot_antisym.py -x1 1 -x2 3 
    
    To run doctests in verbose mode:
    
    python -m doctest -v plot_antisym.py
    
    
'''

def antisym(x1, x2, n1 = 1, n2 = 2, a = 1.0):
    psi = (2/a)*((np.sin(n1*np.pi*x1/a)*np.sin(n2*np.pi*x2/a)) - (np.sin(n1*np.pi*x2/a)*np.sin(n2*np.pi*x1/a)))
    return psi, (psi**2)
    
if __name__ == "__main__":
    import doctest
    import argparse
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-x1', type = float)
    parser.add_argument('-x2', type = float)
    args = parser.parse_args()
    x1 = args.x1
    x2 = args.x2
    
     
    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib import cm
    
    
    fig = plt.figure()
    plt.suptitle('Antisymmetric Spatial Wave Function')
    ax = fig.add_subplot(121, projection = '3d')
    x = y = np.linspace(-x1,x2,100)
    xv, yv = np.meshgrid(x,y)
    wave_f, prob_dens = antisym(xv,yv,n1 = 1, n2 = 2, a = 1.0)#2 rows, 1 column, first of the two
    ax.plot_surface(xv, yv, wave_f, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth = .1)
    fig.subplots_adjust(top=0.85) 
    plt.title('Wave Function')
    ax.set_xlabel('x')
    ax.set_ylabel('y')


    bx = plt.subplot(122, projection ='3d')    
    bx.plot_surface(xv, yv, prob_dens, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth = .1)
    bx.set_xlabel('x')
    bx.set_ylabel('y')
    fig.subplots_adjust(top=0.9)
    plt.title('Probability Density')
    plt.figtext(.07, .03, 'The "effective" interaction between two neutral Fermions (both spin up) that arises from the\n symmetry requirement on the total wave function.')
    

    plt.show()