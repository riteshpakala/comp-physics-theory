from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import copy
from scipy.interpolate import interp2d
import matplotlib.image as mpimg
from scipy import stats
import seaborn as sns; sns.set()
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn import preprocessing
from sklearn.datasets import load_digits

def interpol_im(im, dim1 = 8, dim2 = 8, plot_new_im = False, cmap = 'binary', grid_off = False):
    im = im[:,:,0]
    x = np.arange(im.shape[1])
    y = np.arange(im.shape[0])
    
    f2d = interp2d(x, y, im)
    
    x_new = np.linspace(0, im.shape[1], dim1)
    y_new = np.linspace(0, im.shape[0], dim2)
    
    im_new = f2d(x_new, y_new)
    im_flat = im_new.flatten()
    
    if grid_off == True:
        plt.grid('off')
        
    if plot_new_im == True:
        plt.figure()
        plt.title('Interpolated figure')
        plt.imshow(im_new, cmap = 'gray', interpolation = 'nearest')
        plt.show()
        
    return im_flat
        
def pca_svm_pred(imfile, md_pca, md_clf, dim1 = 45, dim2 = 60):
    init_im = mpimg.imread(imfile)
    interp_im = interpol_im(init_im, dim1, dim2, plot_new_im = True).reshape(1,-1)
    X_proj = md_pca.transform(interp_im)
    return md_clf.predict(X_proj)[0]
    
def pca_X(X, n_comp = 10):
    md_pca = PCA(n_comp, whiten=True)
    md_pca.fit(X)
    X_proj = md_pca.transform(X)
    return md_pca, X_proj

def rescale_pixel(X, unseen, ind = 0):
    Xmax = max(X[ind])
    Xmean = X[ind].mean()
    unseen *= Xmax
    for i in range(len(unseen)):
        unseen[i] = int(unseen[i])
        unseen[i] = 15 - unseen[i]
    return unseen
    
def svm_train(X, y, gamma = 0.001, C = 100.):
    md_clf = svm.SVC(gamma=gamma, C=C)
    md_clf.fit(X, y)
    return md_clf