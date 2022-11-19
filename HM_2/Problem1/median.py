import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

class MedianFilter:
    def __init__(self, img:np.ndarray, winN:int = 5):
        self.img = img
        self.height = img.shape[0]
        self.width = img.shape[1]
        self.winN = winN
        self.padding = self.do_padding()

    def do_padding(self):
        height = self.height
        width = self.width
        
        padded_img = np.zeros((self.img.shape[0]+self.winN-1, self.img.shape[1]+self.winN-1))
        padded_img[self.winN//2:self.winN//2+height, self.winN//2:self.winN//2+width] = self.img
        
        return padded_img

    def get_median(self, i:int, j:int):
        window = self.padding[i-self.winN//2:i-self.winN//2 + self.winN, j-self.winN//2:j-self.winN//2+self.winN]
        median = np.median(window)
        return median

    def do_filter(self):

        print("doing median filter")
        # pad zeros in the edge

        new_img = np.zeros((self.height, self.width))

        for i in tqdm(range(self.winN//2, self.height + self.winN//2)):
            for j in range(self.winN//2, self.width + self.winN//2):
                
                median = self.get_median(i,j)

                # new_img[i-self.winN//2, j-self.winN//2, :] = median
                new_img[i-self.winN//2, j-self.winN//2] = median

        return new_img

if __name__ == "__main__":
    img1 = cv.imread("images\pro1_radiograph_1.jpg", 0)
    img2 = cv.imread("images\pro1_radiograph_2.jpg", 0)

    mf = MedianFilter(img1)
    output = mf.do_filter()
    plt.imshow(output, cmap="gray")
    plt.show()

    ls = [5, 10, 20, 50]
    for windN in ls:
        
        print("window size = ", windN)

        mf_1 = MedianFilter(img1, windN)
        output_img_1 = mf_1.do_filter()

        mf_2 = MedianFilter(img2, windN)
        output_img_2 = mf_2.do_filter()

        