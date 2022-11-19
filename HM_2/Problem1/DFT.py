import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def fft2_plot(img, save_path = None):

    f = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f)
    f_abs = 20*np.log(np.abs(f_shift))


    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Spacial input image')
    plt.subplot(122), plt.imshow(f_abs, cmap = 'gray')
    plt.title('Frequency domain')

    if save_path != None:
        plt.savefig(save_path)

    # plt.show()

    return f_abs


if __name__ == "__main__":
    img1 = cv.imread("images\pro1_radiograph_1.jpg", 0)
    img2 = cv.imread("images\pro1_radiograph_2.jpg", 0)


    fft2_plot(img1, "images\Spacial&Frequencial_1.jpg")
    fft2_plot(img2, "images\Spacial&Frequencial_2.jpg")
    plt.show()
