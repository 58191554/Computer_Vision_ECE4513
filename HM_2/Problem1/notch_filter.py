import cv2 
import numpy as np
from matplotlib import pyplot as plt

def get_fft(img:np.ndarray):

    f = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f)
    f_abs = 20*np.log(np.abs(f_shift))
    return f_abs

def get_notch_filter(ones:np.ndarray, r:int, u, v):

    rows = ones.shape[0]
    cols = ones.shape[1]

    crow = int(rows/2)
    ccol = int(cols/2)

    sym_u = 2*crow - u
    sym_v = 2*ccol - v

    filter = np.ones((rows, cols))

    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i-u)**2 + (j-v)**2)
            sym_dist = np.sqrt((i-sym_u)**2 + (j-sym_v)**2)

            if (dist <= r) or (sym_dist <= r):
                filter[i, j] = 0

    return filter 


def do_notch_1():
    img1 = cv2.imread("images\pro1_radiograph_1.jpg", 0)

    f_abs = get_fft(img1)
    f1 = get_notch_filter(f_abs, 10, 125, 260)
    f2 = get_notch_filter(f_abs, 15, 75, 265)

    f_notch = f_abs*f1*f2

    # plt.subplot(221), plt.imshow(f_notch, cmap = 'gray')
    
    output_img = np.absolute(np.fft.ifft2(np.fft.ifftshift((np.fft.fftshift(np.fft.fft2(img1)))*f1*f2)))
    # plt.subplot(222), plt.imshow(output_img, cmap = 'gray')

    return f_notch, output_img

def do_notch_2():
    img2 = cv2.imread("images\pro1_radiograph_2.jpg", 0)

    f_abs = get_fft(img2)
    f1 = get_notch_filter(f_abs, 10, 440, 280)
    f2 = get_notch_filter(f_abs, 5, 442, 270)

    f_notch = f_abs*f1*f2

    # plt.subplot(223), plt.imshow(f_notch, cmap = 'gray')
    
    output_img = np.absolute(np.fft.ifft2(np.fft.ifftshift((np.fft.fftshift(np.fft.fft2(img2)))*f1*f2)))
    # plt.subplot(224), plt.imshow(output_img, cmap = 'gray')
    return f_notch, output_img


if __name__ == "__main__":
    img1 = cv2.imread("images\pro1_radiograph_1.jpg", 0)
    img2 = cv2.imread("images\pro1_radiograph_2.jpg", 0)

    f_abs = get_fft(img1)

    do_notch_1()
    do_notch_2()

    plt.savefig("images\\notch.jpg")
    plt.show()
