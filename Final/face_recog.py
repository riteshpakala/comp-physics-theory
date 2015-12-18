from pattern_recog_func import *

X = []
y = []
phys_dict = {0: 'Bohr', 1: 'Einstein'}

#In order for .imread to read jpegs or anything other than png, pillow and python 3 is required

for i in range(10):
    im = mpimg.imread('images/bohr'+str(i)+'.jpeg')
    X.append(interpol_im(im, dim1 = 45, dim2 = 60, plot_new_im = False))
    y.append(0)
for i in range(11):
    im = mpimg.imread('images/ein'+str(i)+'.jpeg')
    X.append(interpol_im(im, dim1 = 45, dim2 = 60, plot_new_im = False))
    y.append(1)   

X = np.vstack(X)

count = 0
for i in range(len(y)):
    Xtrain = np.delete(X, i, axis = 0)
    ytrain = np.delete(y, i)
    Xtest = X[i].reshape(1, -1)
    md_pca, X_proj = pca_X(Xtrain, n_comp = 10)#Added whiten attribute to recog func file
    
    Xtrain_proj = md_pca.transform(Xtrain)
    Xtest_proj = md_pca.transform(Xtest)
    md_clf = svm_train(Xtrain_proj,ytrain)
    num = md_clf.predict(Xtest_proj)[0]
    
    if num == y[i]:
        count += 1
    else:
        pass

print('Percentage correct: {:.2f}%, {:d}'.format(100*(float(count)/len(X)), count))

albertbee = pca_svm_pred('images/unseen_phys1.jpg', md_pca, md_clf)
bertbohrbee = pca_svm_pred('images/unseen_phys2.jpg', md_pca, md_clf)
print('PCA+SVM prediction for physicist 1:', phys_dict[albertbee])
print('PCA+SVM prediction for physicist 2:', phys_dict[bertbohrbee])

# comb_img = np.zeros(z[0].shape)
# for i in range(len(y)):
# 	comb_img += z[i]
	
# comb_img /= len(y)

# im2 = mpimg.imread('images/bohr'+str(0)+'.jpeg')
# im = im2[:,:]
# print (im.shape)
# x2 = np.arange(im.shape[1])
# y2 = np.arange(im.shape[0])
# 
# f2d = interp2d(x2, y2, im)
# 
# x_new = np.linspace(0, im.shape[1], 45)
# y_new = np.linspace(0, im.shape[0], 60)
# 
# im_new = f2d(x_new, y_new)
#     
#     
# plt.figure()
# plt.title('Combined')
# plt.imshow(im_new, cmap = 'gray', interpolation = 'nearest')
# plt.show()
# md_pca, X_proj = pca_X(Xtrain, n_comp = 10)
# print md_pca)