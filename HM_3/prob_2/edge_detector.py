import numpy as np
import cv2 
import matplotlib.pyplot as plt
import os
import argparse

def gradientMagnitude(im, sigma, kenel_size = 5):

    N_rows, N_cols, _ = im.shape
    
    smooth=cv2.GaussianBlur(im,(kenel_size,kenel_size),sigma)
    sobelx = cv2.Sobel(smooth,cv2.CV_64F,1,0)
    sobely = cv2.Sobel(smooth,cv2.CV_64F,0,1)

    gm = np.sqrt(sobelx ** 2 + sobely ** 2)
    print(gm.shape)
    mag = np.sqrt(np.square(gm[:, :, 0]) + np.square(gm[:, :, 1]) + np.square(gm[:, :, 2]))

    #  The orientation can be computed from the channel corresponding to the largest gradient magnitude. 
    theta = np.zeros((N_rows, N_cols))
    for i in range(N_rows):
        for j in range(N_cols):
            a = np.argmax([gm[i, j, 0], gm[i, j, 1], gm[i, j, 2]])
            gx = sobelx[i, j, a]
            gy = sobely[i, j, a]
            theta[i, j] = np.arctan(gy/gx)


    # plt.subplot(121), plt.imshow(mag/np.max(mag)*255, cmap="gray"), plt.title("mag")
    # plt.subplot(122), plt.imshow(theta), plt.title("theta")
    # plt.show()
    return mag, theta

def non_max_suppression(img, theta):
    N_rows, N_cols = img.shape
    suppress = np.zeros((N_rows,N_cols))
    angle = theta * 180. / np.pi
    angle[angle < 0] += 180

    
    for i in range(1,N_rows-1):
        for j in range(1,N_cols-1):
            q = 255
            r = 255
            
            # angle 0
            if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                q = img[i, j+1]
                r = img[i, j-1]
            #angle 45
            elif (22.5 <= angle[i,j] < 67.5):
                q = img[i+1, j-1]
                r = img[i-1, j+1]
            #angle 90
            elif (67.5 <= angle[i,j] < 112.5):
                q = img[i+1, j]
                r = img[i-1, j]
            #angle 135
            elif (112.5 <= angle[i,j] < 157.5):
                q = img[i-1, j-1]
                r = img[i+1, j+1]

            if (img[i,j] >= q) and (img[i,j] >= r):
                suppress[i,j] = img[i,j]
            else:
                suppress[i,j] = 0

    # plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("input")
    # plt.subplot(122), plt.imshow(suppress, cmap="gray"), plt.title("non_max_suppression")
    # plt.show()
    return suppress

def threshold(img, lowThresholdRatio=0.05, highThresholdRatio=0.2, weak = 100, strong = 255):
    
    highThreshold = img.max() * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio
    
    N_rows, N_cols = img.shape
    res = np.zeros((N_rows,N_cols), dtype=np.int32)
        
    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    res[zeros_i, zeros_j] = 0

    # plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("input")
    # plt.subplot(122), plt.imshow(res, cmap="gray"), plt.title("doublr threshold")
    # plt.show()
    return res

def hysteresis(img, weak = 100, strong = 255):

    N_rows, N_cols = img.shape
    new_img = np.zeros((N_rows, N_cols))

    for i in range(1, N_rows-1):
        for j in range(1, N_cols-1):
            if(img[i, j] == weak):
                patch = img[i-1:i+1, j-1:j+1]
                if(
                    img[i-1, j-1] == strong or
                    img[i-1, j] == strong or
                    img[i-1, j+1] == strong or
                    img[i, j-1] == strong or
                    img[i, j+1] == strong or
                    img[i+1, j-1] == strong or
                    img[i+1, j] == strong or 
                    img[i+1, j+1] == strong                 
                ):
                    new_img[i, j] = 255

                else:
                    new_img[i, j] = 0

            else:
                new_img[i,j] = img[i, j]

    # plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("input")
    # plt.subplot(122), plt.imshow(new_img, cmap="gray"), plt.title("Edge Tracking by Hysteresis")
    # plt.show()
    return new_img


def edgeGradient(im):
    mag, theta = gradientMagnitude(im, 1)
    non_sprs_img = non_max_suppression(mag/np.max(mag)*255, theta)
    threshold_img = threshold(non_sprs_img)
    bmap = hysteresis(threshold_img)
    plt.imshow(bmap, cmap="gray")
    plt.show()
    return bmap


def Conv2D(img, kernel:np.ndarray):

    N_rows, N_cols = img.shape
    kernel_size, _ = kernel.shape
    a =(kernel_size-1)//2

    # padding
    padded = np.zeros((N_rows+kernel_size-1, N_cols + kernel_size-1))

    padded[a:a+N_rows, a:a+N_cols] = img

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


def orientedFilterMagnitude(im): 

    if(len(im.shape) == 3):
        N_rows, N_cols, _ = im.shape
    else:
        N_rows, N_cols = im.shape

    if(len(im.shape) == 3):
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    kernel_a = np.array([
        [0, -1, -2],
        [1, 0, -1],
        [2, 1, 0]
    ])
    kernel_b = np.array([
        [2, 1, 0],
        [1, 0, -1],
        [0, -1, -2]
    ])
    kernel_x = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])
    kernel_y = np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ])

    ga = Conv2D(im, kernel_a)
    gb = Conv2D(im, kernel_b)
    gx = Conv2D(im, kernel_x)
    gy = Conv2D(im, kernel_y)

    # mag = np.sqrt(np.square(ga) + np.square(gb) + np.square(gx) + np.square(gy))
    mag = np.zeros(im.shape)
    for i in range(N_rows):
        for j in range(N_cols):
            mag[i, j] = np.max([ga[i, j], gb[i, j], gx[i, j], gy[i, j]])
        
    theta = np.zeros(im.shape)

    # clock wise 
    for i in range(N_rows):
        for j in range(N_cols):
            theta_index = np.argmax([gx[i, j], ga[i, j], -gy[i, j], -gb[i, j], -gx[i, j], -ga[i, j], gy[i, j], gb[i, j]])
            theta[i, j] = theta_index/8*np.pi/4

    return mag, theta

def edgeOrientedFilters(im):

    mag, theta = orientedFilterMagnitude(im)
    non_sprs_img = non_max_suppression(mag/np.max(mag)*255, theta)
    threshold_img = threshold(non_sprs_img)
    bmap = hysteresis(threshold_img)
    plt.imshow(bmap, cmap="gray")
    # plt.savefig("edge_Oriented_Filters.jpg")
    plt.show()
    return bmap

def task_a(read_dir, write_dir):
    for filename in os.listdir(r"./"+read_dir):
        if(filename[-4:] != ".jpg"):
            continue
        img = cv2.imread(read_dir + "/" + filename)
        print(read_dir + "/" + filename)
        bmap = edgeGradient(img)
        cv2.imwrite(write_dir+ "/"+ filename[:-4]+".png", bmap)

def task_b(read_dir, write_dir):
    for filename in os.listdir(r"./"+read_dir):
        if(filename[-4:] != ".jpg"):
            continue
        img = cv2.imread(read_dir + "/" + filename)
        print(read_dir + "/" + filename)
        bmap = edgeOrientedFilters(img)
        cv2.imwrite(write_dir+ "/"+ filename[:-4]+".png", bmap)

if __name__ == "__main__":
    # img = cv2.imread(r"data/images/test/2018.jpg") 
    # bmap = edgeGradient(img)
    # bmap = edgeOrientedFilters(img)

    read_dir = "data/images/test"
    write_dir = "data/png/test"


    parser = argparse.ArgumentParser(description='task a or b')
    parser.add_argument('task', type=str, help='task_a or task_b')
    args = parser.parse_args()


    if(args.task == "task_a"):
        # task (a)
        task_a(read_dir, write_dir)

    if(args.task == "task_b"):
        # task (b)
        task_b(read_dir, write_dir)
