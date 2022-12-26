import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import random
import argparse


def non_max_suppression(img, path_size = 5):

    N_rows, N_cols = img.shape
    suppress = np.zeros(img.shape)

    for i in range(2, N_rows-2):
        for j in range(2, N_cols-2):
            patch = img[i-2:i+3, j-2:j+3]
            if(img[i,j] < np.max(patch)):
                continue
            else:
                suppress[i,j] = img[i,j]

    # plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("input")
    # plt.subplot(122), plt.imshow(suppress), plt.title("suppress")
    # plt.show()

    return suppress

def harrgetKeypointsis(img, tau = 10000000):

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    N_rows, N_cols = img.shape

    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
    sigma = 0
    Ixx = cv2.GaussianBlur(sobelx**2, (5, 5), sigma)
    Ixy = cv2.GaussianBlur(sobelx*sobely, (5, 5), sigma)
    Iyy = cv2.GaussianBlur(sobely**2, (5, 5), sigma)

    a = 0.05
    # determinant
    detM = Ixx * Iyy - Ixy ** 2
    # trace
    traceM = Ixx + Iyy
    
    harris_response = detM - a * traceM ** 2

    for i in range(N_rows):
        for j in range(N_cols):
            if(harris_response[i,j] > -tau and harris_response[i,j]<tau):
                harris_response[i,j] = 0

    harris_response = non_max_suppression(harris_response)

    keyXs = []
    keyYs = []
    for i in range(N_rows):
        for j in range(N_cols):
            if harris_response[i,j] > 0:
                # this is a corner
                keyXs.append(i)
                keyYs.append(j)
            # elif r < 0:
            #     # this is an edge
            #     img_copy_for_edges[i, j] = [0,255,0]

    plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("input")
    plt.subplot(122), plt.imshow(img, cmap="gray"), plt.title("corners")
    plt.scatter(keyYs, keyXs, c="r", s=1)
    plt.show()
    plt.savefig("harrget_Keypointsis.jpg")
    return keyXs, keyYs

def check_out(N_rows, N_cols, x, y):

    patch_size = 15
    offset = 7

    if(x-offset < 0 or x-offset+patch_size >= N_rows or y-offset < 0 or y-offset+patch_size >= N_cols):
        return True 

    else:
        return False

def interpolate(img, x, y):
    # input an image and output a 15x15 interpolate patch

    u = x-math.floor(x)
    v = y-math.floor(y)

    # plt.subplot(121), plt.imshow(img[math.floor(x)-7:math.floor(x)+8, math.floor(y)-7:math.floor(y)+8])
    try:
        patch_inter = np.zeros((15, 15))
        for i in range(15):
            for j in range(15):
                p = int(x-7-u+i)
                q = int(y-7-v+j)
                patch_inter[i, j] = (img[p, q]*(1-v) + img[p, q+1]*v) * (1-u)+\
                                    (img[p+1,q]*(1-v)+ img[p+1,q+1]*v) * (u)
        # plt.subplot(122), plt.imshow(patch_inter)
        # plt.show()
        return patch_inter
    except:
        return None

def predictTranslationAll(keyXs, keyYs, im0, im1):

    print("{} points to track".format(len(keyXs)))

    N_rows, N_cols = im0.shape

    # blur with Gaussian
    im0 = cv2.GaussianBlur(im0, (5, 5), 0)
    im1 = cv2.GaussianBlur(im1, (5, 5), 0)

    W_size = 15
    offset = (W_size-1)//2

    sobelx = cv2.Sobel(im0,cv2.CV_64F,1,0)
    sobely = cv2.Sobel(im0,cv2.CV_64F,0,1)

    newXs, newYs = np.copy(keyXs).astype(float), np.copy(keyYs).astype(float)
    out_point = []
    outXs = []
    outYs = []

    iter_max = 30

    for i in range(len(keyXs)):
        x = int(keyXs[i])
        y = int(keyYs[i])

        patch_Ix = sobelx[x-offset:x+offset+1, y-offset:y+offset+1]
        patch_Iy = sobely[x-offset:x+offset+1, y-offset:y+offset+1]
        A = np.array([[np.sum(patch_Ix * patch_Ix), np.sum(patch_Ix * patch_Iy)], [np.sum(patch_Ix * patch_Iy), np.sum(patch_Iy * patch_Iy)]])
        for j in range(iter_max):
            _x = newXs[i]
            _y = newYs[i]

            if(check_out(N_rows, N_cols, _x, _y)):
                out_point.append(i)
                break
            patch_next = interpolate(im1, _x, _y)
            patch_now = im0[x-offset:x+offset+1, y-offset:y+offset+1]
            patch_It = patch_next - patch_now
            b =  -1* np.array([[np.sum(patch_Ix*patch_It)],[np.sum(patch_Iy*patch_It)]])
            solution = np.linalg.solve(A, b)

            u = solution[1]
            v = solution[0]

            newXs[i] = newXs[i] + u
            newYs[i] = newYs[i] + v

            if np.sqrt(u**2+ v**2) <= 0.01:
                break      

    for i in range(len(out_point)-1, -1, -1):
        pop_index = out_point[i]
        print("move out:", pop_index)
        outXs.append(newXs[pop_index])
        outYs.append(newYs[pop_index])

        newXs = np.delete(newXs, pop_index)
        newYs = np.delete(newYs, pop_index)

    return newXs, newYs, outXs, outYs


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='track_num')
    parser.add_argument('track_num', type=int, help='input track_num', default=20)
    args = parser.parse_args()

    # task a

    img_src = r"images\hotel.seq0.png"
    img = cv2.imread(img_src, 0)
    print(img.shape)
    keyXs, keyYs = harrgetKeypointsis(img)

    if(args.track_num > len(keyXs)):
        print("Too many points to track!")

    # task b
    else:

        im1 = cv2.imread(r"images\hotel.seq1.png", 0)

        random_index = random.sample(range(len(keyXs)), args.track_num)
        print(random_index)

        StartXs = [keyXs[i] for i in random_index]
        StartYs = [keyYs[i] for i in random_index]

        plt.subplot(121)
        plt.imshow(img, cmap="gray"), plt.title("1 step")
        plt.scatter(StartYs, StartXs, s=6, c='w', marker='o', edgecolors='g')
        newXs, newYs, outXs, outYs= predictTranslationAll(StartXs, StartYs, img, im1)
        plt.scatter(newYs, newXs, s=1, c='r')
        plt.subplot(122), plt.imshow(im1, cmap="gray"), plt.title("50 step")
        plt.scatter(StartYs, StartXs, s=8, c='w', marker='o', edgecolors='g')

        im_t = img
        for i in range(1, 51):
            print("round: ", i)
            im_next = cv2.imread(r"images\hotel.seq"+ str(i)+".png", 0)
            newXs, newYs, outXs, outYs = predictTranslationAll(StartXs, StartYs, im_t, im_next)
            plt.scatter(newYs, newXs, s=1, c="r")
            plt.scatter(outYs, outXs, s=8, c='b')
            im_t = im_next

            if(len(keyXs) == 0 or len(keyYs) == 0):
                break

            StartXs, StartYs = newXs, newYs

        plt.savefig(str(args.track_num)+"track.jpg")
        plt.show()
