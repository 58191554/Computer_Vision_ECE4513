import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import ginput


def getVanishingPoint(im):
    lines = np.zeros((0, 3))
    line_length = []
    centers = np.zeros((0, 3))

    plt.imshow(im)

    while True:
        print(' ')
        print('Click first point or click the same point twice to stop')
        
        x1,y1 = ginput(1)[0]
        print("report x1 = %f, y1 = %f".format( x1, y1))
        
##        if b=='q':      
##            break
        
        print('Click second point')
        x2,y2 = ginput(1)[0]
        plt.plot([x1, x2], [y1, y2], 'b')

        length = np.sqrt((y2-y1)**2 + (x2-x1)**2)
        if length < 0.0001:
            break
        
        lines = np.vstack([lines, np.cross(np.array([x1, y1, 1]).reshape(1, 3),
                                   np.array([x2, y2, 1]).reshape(1, 3))])
        
        line_length.append(length)
        centers = np.vstack([centers, np.array([x1+x2, y1+y2, 2]).reshape(1, 3)/2])

    print('find VP')
    # insert code here to compute vp (3-d vector in homogeneous coordinates)

    bx1 = min(1, vp[0] / vp[2]) - 10
    bx2 = max(im.shape[1], vp[0] / vp[2]) + 10
    by1 = min(1, vp[1] / vp[2]) - 10
    by2 = max(im.shape[0], vp[1] / vp[2]) + 10
    for k  in range(lines.shape[0]):
        if lines[k, 0] < lines[k, 1]:
            pt1 = np.cross(np.array([1, 0, -bx1]).reshape(1, 3), lines[k])
            pt2 = np.cross(np.array([1, 0, -bx2]).reshape(1, 3), lines[k])
        else:
            pt1 = np.cross(np.array([0, 1, -by1]).reshape(1, 3), lines[k])
            pt2 = np.cross(np.array([0, 1, -by2]).reshape(1, 3), lines[k])

        pt1 = pt1 / pt1[2]
        pt2 = pt2 / pt2[2]
        
        plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], 'g', 'Linewidth', 1)
    pass
    


if __name__ == "__main__":
    im = plt.imread('./kyoto_street.JPG')
    getVanishingPoint(im)
    plt.show()


