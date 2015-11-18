import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def extract_shape(im_file, blowup = 1., plot_img = False, plot_contour = False, plot_contour_pts = False):
    x_arr = []
    y_arr = []
    im = mpimg.imread(im_file)
    if len(im.shape) > 2:
        im = im[:, :, 0]
    
    if plot_img:
        plt.figure()
        plt.title('Original Shape')
        plt.imshow(im, cmap = plt.cm.gray)

    x = np.arange(im.shape[1])*blowup  
    y = np.arange(im.shape[0])*blowup
    
    y = y[::-1]

    X, Y = np.meshgrid(x, y)
    
    plt.figure()
    plt.title('Contours')
    CS = plt.contour(X, Y, im, 1)
    levels = CS.levels
    print 'contour level', levels
    if not plot_contour:
        plt.close()

    cs_paths = CS.collections[0].get_paths()
    global cs_paths
    print 'number of contour path', len(cs_paths)

    for i in range(0, len(cs_paths)):
        v = cs_paths[i].vertices
        x_arr.append(v[:,0])
        y_arr.append(v[:,1])

    if plot_contour_pts:
        plt.figure()
        plt.title("Verify the contour points are correct")
        for i in range(0, len(cs_paths)):
            plt.scatter(x_arr[i], y_arr[i])

    return x_arr, y_arr

def FD(x, y, plot_FD = False, y_lim = None):
    N = len(x)
    n = np.arange(N)
    z = x + y*1j
    Z = np.fft.fft(z)
    if plot_FD:
        plt.figure()
        plt.title('FD real and imag')
        plt.plot(Z.real, 'b-')
        plt.plot(Z.imag, 'g-')
        if y_lim != None:
            plt.ylim([-y_lim, y_lim])
    return Z
    
def filt_FD(Z, n_keep, no_zeroth = True):
    N = len(Z)
    n = np.arange(len(Z))
    print 'Nyquist index', N/2
    filt0 = n > 0 if no_zeroth else 1
    filt1 = filt0*(n <= n_keep)
    
    filt2 = (n > ((N-1) - n_keep))
    print 'Number of components from both sides:', filt1.sum(), filt2.sum()
    filt = filt1 + filt2
    return Z*filt
    
def get_FD_abs(x, y, order = 10, norm = True, no_zeroth = True):
    x = []     
    y = []
    fd_mag = []
    for i in range(len(x)):  
        Z = FD(x[i], y[i])
        Z_filt = filt_FD(Z, order, no_zeroth)
        if norm:
            Z_filt = size_norm(Z_filt)
        x_rec, y_rec = recover_shape(Z_filt)
        tmp_mag = []
        for i in Z_filt:           
            if i != 0:
                tmp_mag.append(i)
        mag = np.abs(tmp_mag)    
        x.append(x_rec)
        y.append(y_rec)
        fd_mag.append(mag)
    return fd_mag, x, y

def recover_shape(Z):
    z_rec = np.fft.ifft(Z)
    x_rec = z_rec.real
    y_rec = z_rec.imag
    return x_rec, y_rec
    
def size_norm(Z):
    return Z/np.sqrt(np.abs(Z[1])*np.abs(Z[-1]))
    
def plot_shape(x, y, ax = 0, plot_style = 'b.', new_plot = False):
    if new_plot == True:
        fig, ax = plt.subplots()
        ax.set_title('Recovered Shape')
    try:
        xlen = len(x)
    except:
        ax.plot(x, y, plot_style)
    else:
        for i in range(xlen):
            ax.plot(x[i], y[i], plot_style)
    return ax

x1, y1 = extract_shape('number1.png')
x2, y2 = extract_shape('number2.png')
x6, y6 = extract_shape('number6.png')

fd1_mag, x1_rec, y1_rec = get_FD_abs(x1, y1)
fd2_mag, x2_rec, y2_rec = get_FD_abs(x2, y2)
fd6_mag, x6_rec, y6_rec = get_FD_abs(x6, y6)

plt.figure()
plt.xlim(-.02, .02)
plt.ylim(-.02, .02)
plt.title("Numbers Recovered From FD's")
for i in range(len(x1_rec)):
	plt.plot(y1_rec[i], x1_rec[i], 'b')
for i in range(len(x2_rec)):
	plt.plot(x2_rec[i], y2_rec[i], 'g')
for i in range(len(x6_rec)):
	plt.plot(x6_rec[i], y6_rec[i], 'r')
plt.savefig('rec_numbers126.pdf')
plt.show()

plt.figure()
plt.title("Magnitudes of FD's for 1, 2, and 6")
plt.xlim(0, 2*10)
for i in range(len(fd1_mag)):
	plt.plot(np.arange(2, 20), fd1_mag[i][1:-1], 'bo')
for i in range(len(fd2_mag)):
	plt.plot(np.arange(2, 20), fd2_mag[i][1:-1], 'gx')
for i in range(len(fd6_mag)):
	plt.plot(np.arange(2, 20), fd6_mag[i][1:-1], 'r^')
plt.savefig('FourierDescriptor_numbers126.pdf')
plt.show()