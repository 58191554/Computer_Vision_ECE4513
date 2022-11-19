import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

from median import MedianFilter
from notch_filter import do_notch_1, do_notch_2

if __name__ == "__main__":

    img1 = cv.imread("images\pro1_radiograph_1.jpg", 0)
    img2 = cv.imread("images\pro1_radiograph_2.jpg", 0)

    # Problem(a)
    # window size = 8
    mf_1 = MedianFilter(img1, 8)
    median_1 = mf_1.do_filter()
    # window size = 13
    mf_2 = MedianFilter(img2, 13)
    median_2 = mf_2.do_filter()

    plt.subplot(121), plt.imshow(median_1, cmap="gray"), plt.title("img1 median filter size = 8")
    plt.subplot(122), plt.imshow(median_2, cmap="gray"), plt.title("img2 median filter size = 13")
    plt.savefig("images\problem(a).jpg")
    plt.show()

    # Problem(b)
    plt.subplot(221),plt.imshow(img1, cmap="gray"), plt.title("img1 original Spacial Domian")
    plt.subplot(222),plt.imshow(20*np.log(np.abs(np.fft.fftshift(np.fft.fft2(img1)))), cmap = 'gray')
    plt.title('img1 Frequency Domian')

    plt.subplot(223),plt.imshow(img2, cmap="gray"), plt.title("img2 original Spacial Domian")
    plt.subplot(224),plt.imshow(20*np.log(np.abs(np.fft.fftshift(np.fft.fft2(img2)))), cmap = 'gray')
    plt.title('img2 Frequency Domian')
    plt.savefig("images\problem(b).jpg")

    plt.show()


    # Problem(c)

    f_notch_1, output_img_1 = do_notch_1()
    f_notch_2, output_img_2 = do_notch_2()

    plt.subplot(221), plt.imshow(f_notch_1, cmap="gray"), plt.title("img1 Notch Frequency Domian")
    plt.subplot(222), plt.imshow(output_img_1, cmap="gray"), plt.title("img1 Notch Spacial Domian")

    plt.subplot(223), plt.imshow(f_notch_2, cmap="gray"), plt.title("img2 Notch Frequency Domian")
    plt.subplot(224), plt.imshow(output_img_2, cmap="gray"), plt.title("img2 Notch Spacial Domian")

    plt.savefig("images\problem(c).jpg")

    plt.show()
