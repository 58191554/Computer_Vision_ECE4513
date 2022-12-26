import cv2
import numpy as np
import matplotlib.pyplot as plt

def Gaussian_Conv(img, kernel_size:int, gaus_sigma = 0.8):

    N_rows, N_cols = img.shape
    a =(kernel_size-1)//2

    if kernel_size%2 == 0:
        kernel_size += 1
    gaussian = lambda x, y: 1/(2*np.pi*gaus_sigma**2) * np.exp(- ((x-a)**2 + (y-a)**2)/ (2 * gaus_sigma**2))
    kernel = np.array([[gaussian(i, j) for i in range(kernel_size)] for j in range(kernel_size)])
    # print(kernel)
    
    # padding
    padded = np.zeros((N_rows+kernel_size-1, N_cols + kernel_size-1))

    padded[a:a+N_rows, a:a+N_cols] = img
    # print(padded.shape)

    conv_img = np.zeros((N_rows, N_cols))
    for i in range(N_rows):
        for j in range(N_cols):
            sub_img = padded[i:i+kernel_size, j:j+kernel_size]
            # print(i, j, sub_img.shape)
            new_pixel = np.sum(kernel * sub_img)
            conv_img[i, j] = new_pixel

    # plt.subplot(121), plt.imshow(img, cmap="gray")
    # plt.subplot(122), plt.imshow(conv_img, cmap="gray")
    # plt.show()

    return conv_img

def down_sample(img):
    N_rows, N_cols = img.shape
    
    new_img = np.zeros((N_rows//2, N_cols//2))

    for i in range(N_rows//2):
        for j in range(N_cols//2):
            new_img[i, j] = img[2*i, 2*j]

    # plt.subplot(121), plt.imshow(img, cmap="gray")
    # plt.subplot(122), plt.imshow(new_img, cmap="gray")
    # plt.show()

    return new_img

def Gauss_pyramid(img):
    g1 = down_sample(Gaussian_Conv(img, 11))
    g2 = down_sample(Gaussian_Conv(g1, 11))
    g3 = down_sample(Gaussian_Conv(g2, 11))
    g4 = down_sample(Gaussian_Conv(g3, 11))
    g5 = down_sample(Gaussian_Conv(g4, 11))

    plt.subplot(161), plt.imshow(img, cmap="gray"), plt.title("original")
    plt.subplot(162), plt.imshow(g1, cmap="gray"), plt.title("g1")
    plt.subplot(163), plt.imshow(g2, cmap="gray"), plt.title("g2")
    plt.subplot(164), plt.imshow(g3, cmap="gray"), plt.title("g3")
    plt.subplot(165), plt.imshow(g4, cmap="gray"), plt.title("g4")
    plt.subplot(166), plt.imshow(g5, cmap="gray"), plt.title("g5")
    plt.show()

    return (img, g1, g2, g3, g4, g5)

def expand(img):
    N_rows, N_cols = img.shape
    expand_img = np.zeros((2*N_rows, 2*N_cols))
    for i in range(N_rows):
        for j in range(N_cols):
            pixel = img[i, j]
            expand_img[2*i, 2*j] = pixel
            expand_img[2*i+1, 2*j] = pixel
            expand_img[2*i, 2*j+1] = pixel
            expand_img[2*i+1, 2*j+1] = pixel

    return expand_img

def get_laplacian(g, e):
    # just minus but want to regularize their size
    N_g_rows, N_g_cols = g.shape
    N_e_rows, N_e_cols = e.shape

    N_rows = max(N_g_rows, N_e_rows)
    N_cols = max(N_g_cols, N_e_cols)

    new_g = np.zeros((N_rows, N_cols))
    new_g[:N_g_rows, :N_g_cols] = g
    new_e = np.zeros((N_rows, N_cols))
    new_e[:N_e_rows, :N_e_cols] = e

    laplacian = new_g-new_e
    return laplacian

def Laplacian_Pyramid(G_pyramid):
    g0, g1, g2, g3, g4, g5 = G_pyramid
    
    l4 = get_laplacian(g4, expand(g5))
    l3 = get_laplacian(g3, expand(g4))
    l2 = get_laplacian(g2, expand(g3))
    l1 = get_laplacian(g1, expand(g2))
    l0 = get_laplacian(g0, expand(g1))

    plt.subplot(151), plt.imshow(l0, cmap="gray"), plt.title("l0")
    plt.subplot(152), plt.imshow(l1, cmap="gray"), plt.title("l1")
    plt.subplot(153), plt.imshow(l2, cmap="gray"), plt.title("l2")
    plt.subplot(154), plt.imshow(l3, cmap="gray"), plt.title("l3")
    plt.subplot(155), plt.imshow(l4, cmap="gray"), plt.title("l4")
    plt.show()

    return l0, l1, l2, l3, l4

def fft2_plot(img, save_path = None, lable = "g"):

    f = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f)
    f_abs = 20*np.log(np.abs(f_shift))

    plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("Spatial "+ lable)
    plt.subplot(122), plt.imshow(f_abs, cmap="gray"), plt.title("Frequncial " + lable)

    if save_path != None:
        plt.savefig(save_path)

    # plt.show()

    return f_abs


if __name__ == "__main__":
    img_src = r"cat.jpg"
    img = cv2.imread(img_src)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(img, cmap ='gray')
    # plt.show()
    print(img.shape)
    # Gaussian_Conv(img, 5)
    # down_sample(img)
    g_p = Gauss_pyramid(img)
    l_p = Laplacian_Pyramid(g_p)

    for i in range(len(g_p)):
        g_i = g_p[i]
        g_i_f = fft2_plot(g_i, "Gaussain Fourier" + str(i) + ".jpg", lable="g"+str(i))

    for i in range(len(l_p)):
        l_i = l_p[i]
        l_i_f = fft2_plot(l_i, "Laplacian Fourier" + str(i) + ".jpg", lable="l"+str(i))
    

