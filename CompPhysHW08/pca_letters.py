from __future__ import print_function, division
import argparse 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import stats
import seaborn as sns; sns.set()
from sklearn.decomposition import PCA
from scipy.interpolate import interp2d

parser = argparse.ArgumentParser()
parser.add_argument('-let_idx', type = int) 
parser.add_argument('-n_comp', type = int)
args = parser.parse_args()
let_idx = args.let_idx
n_comp = args.n_comp

def alphabet_pca(X, n_comp = n_comp):
    pca = PCA(n_comp)  
    Xproj = pca.fit_transform(X)
    pca_comps = pca.components_
    return pca, Xproj, pca_comps

def make_let_im(let_file, dim = 16, y_lo = 70, y_hi = 220, x_lo = 10, \
               x_hi = 200, edge_pix = 148, plot_let = False):
    init_im = mpimg.imread(let_file)
    im = init_im[y_lo:y_hi,x_lo:x_hi]
    im[:,edge_pix:] = 1
    im_2d = im[:,:,0]
    x = np.arange(im_2d.shape[1])
    y = np.arange(im_2d.shape[0])
    f2d = interp2d(x, y, im_2d)
    x_new = np.linspace(0, im_2d.shape[1], 16)
    y_new = np.linspace(0, im_2d.shape[0], 16)
    let_im = f2d(x_new, y_new)
    let_im_flat = np.concatenate(let_im)
    if plot_let == True:
        plt.figure()
        plt.title('Interpolated Letter')
        plt.grid('off')
        plt.imshow(let_im, cmap = 'binary')
        plt.show()
    return let_im, let_im_flat

def show_pca_im(Xproj, pca_comps, dim = 16, n_comp = n_comp, let_idx = let_idx):
    dig_im = np.zeros((dim, dim))
    coeffs = Xproj[let_idx]
    f, axes = plt.subplots(1, n_comp, figsize = (10, 2), subplot_kw=dict(xticks=[], yticks=[]))
    for i in range(n_comp):
        axes[i].imshow(coeffs[i]*pca_comps[i].reshape((16, 16)), cmap='binary')
    for i in range(n_comp):
        dig_im += coeffs[i]*pca_comps[i].reshape((16, 16))
        
    fig, ax = plt.subplots(1, 1, figsize = (2, 2))
    ax.imshow(dig_im, cmap='binary')
    ax.grid(False)
    ax.axis('off')
    plt.show()
  
A, A_flat = make_let_im('letterA.png', edge_pix = 135)
B, B_flat = make_let_im('letterB.png', edge_pix = 130)
C, C_flat = make_let_im('letterC.png', edge_pix = 125)
D, D_flat = make_let_im('letterD.png', edge_pix = 140)
E, E_flat = make_let_im('letterE.png', edge_pix = 118)
F, F_flat = make_let_im('letterF.png', edge_pix = 115)
G, G_flat = make_let_im('letterG.png', edge_pix = 145)
H, H_flat = make_let_im('letterH.png', edge_pix = 145)
I, I_flat = make_let_im('letterI.png', edge_pix = 145)
J, J_flat = make_let_im('letterJ.png', edge_pix = 85)
K, K_flat = make_let_im('letterK.png', edge_pix = 125)
L, L_flat = make_let_im('letterL.png', edge_pix = 105)
M, M_flat = make_let_im('letterM.png', edge_pix = 180)
N, N_flat = make_let_im('letterN.png', edge_pix = 140)
O, O_flat = make_let_im('letterO.png', edge_pix = 155)
P, P_flat = make_let_im('letterP.png', edge_pix = 125)
Q, Q_flat = make_let_im('letterQ.png', edge_pix = 170)
R, R_flat = make_let_im('letterR.png', edge_pix = 130)
S, S_flat = make_let_im('letterS.png', edge_pix = 115)
T, T_flat = make_let_im('letterT.png', edge_pix = 120)
U, U_flat = make_let_im('letterU.png', edge_pix = 150)
V, V_flat = make_let_im('letterV.png', edge_pix = 135)
W, W_flat = make_let_im('letterW.png', edge_pix = 220)
X, X_flat = make_let_im('letterX.png', edge_pix = 125)
Y, Y_flat = make_let_im('letterY.png', edge_pix = 120)
Z, Z_flat = make_let_im('letterZ.png', edge_pix = 115)

X = np.array([A_flat,B_flat,C_flat,D_flat,E_flat,F_flat,G_flat,\
             H_flat,I_flat,J_flat,K_flat,L_flat,M_flat,N_flat,\
             O_flat,P_flat,Q_flat,R_flat,S_flat,T_flat,U_flat,V_flat,\
             W_flat,X_flat,Y_flat,Z_flat])

alfbet_pca, XProj, pca_comps = alphabet_pca(X)

let_coef = show_pca_im(XProj, pca_comps)