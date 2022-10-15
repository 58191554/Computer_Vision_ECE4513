from re import T
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import ginput

from getVanishingPoint import Line, getVanishingPoint, get_horizon_line, get_line_cross

POINTS = [
        [92.27310924369749, 2421.8193277310925, 1439.5,  2120.642857142857],
        [124.54201680672304, 2491.735294117647, 1482.5252100840335, 2171.735294117647],
        [1391.0966386554624, 2308.878151260504, 1197.4831932773109, 2236.2731092436975],
        [1329.247899159664, 2206.6932773109243, 1495.9705882352941, 2263.1638655462184],
        [933.953781512605, 1986.189075630252, 955.7100840336134, 918.6260504201682],
        [1194.794117647059, 2026.5252100840337, 1190.1722689075632, 1058.4579831932774]
    ]


def select_line():
    print('Click first point or click the same point twice to stop')

    x1,y1 = ginput(1)[0]

    print("report x1 = {}, y1 = {}".format( x1, y1))
    
    print('Click second point')
    x2,y2 = ginput(1)[0]
    print("report x2 = {}, y2 = {}".format( x2, y2))

    new_line = Line(x1, y1, x2, y2)
    new_line.plot_line()
    return new_line

def vertical_vertify(line:Line, horz_line:Line):
    
    pass

def getHeight(sign:Line, target:Line, horz_line:Line, real_H:float):

    # connect the bottom
    bottom_line = Line(sign.bottom[0], sign.bottom[1], target.bottom[0], target.bottom[1])
    bottom_line.plot_line()
    vp = get_line_cross(bottom_line, horz_line)

    # connect the vanishing point and the sign tip
    tip_line = Line(vp[0], vp[1], sign.tip[0], sign.tip[1])
    tip_line.plot_line()
    t_cross_pt = get_line_cross(tip_line, target)
    t_cross_line = Line(target.bottom[0], target.bottom[1], t_cross_pt[0], t_cross_pt[1])

    height = real_H*target.length/t_cross_line.length

    return height

def get_cameraH(sign:Line, horz_line:Line, real_H:float):

    intsct = get_line_cross(sign, horz_line)
    intsct_bot = Line(intsct[0], intsct[1], sign.bottom[0], sign.bottom[1])
    
    height = (intsct_bot.length/sign.length) * real_H
    print("the camera height = %f"%(height))
    return height

if __name__ == "__main__":
    
    new_im = plt.imread("./CIMG6476.JPG")
    vps = getVanishingPoint(new_im, False, POINTS)

    horz_line = get_horizon_line(vps[0], vps[1])

    plt.cla()
    # plt.show()

    sign_line = Line(1036.138655462185, 2195.936974789916, 1036.138655462185, 2053.415966386555)
    Tractor_line = Line(1754.1218487394958, 2308.878151260504, 1762, 2105)
    Building_line = Line(933.953781512605, 1991.5672268907563, 942.0210084033615, 915.9369747899159)
    
    real_h = 1.65

    plt.text(sign_line.tip[0], sign_line.tip[1], str(1.65))
    building_h = getHeight(sign_line, Building_line, horz_line, real_h )
    plt.text(Building_line.tip[0], Building_line.tip[1], str(building_h) )
    print("the height of building is %f"%(building_h))

    plt.text(sign_line.tip[0], sign_line.tip[1], str(1.65))
    tractor_h = getHeight(sign_line, Tractor_line, horz_line, real_h )
    plt.text(Tractor_line.tip[0], Tractor_line.tip[1], str(tractor_h) )
    print("the height of tractor is %f"%(tractor_h))

    plt.imshow(new_im)
    sign_line.plot_line(), Tractor_line.plot_line(), Building_line.plot_line()
    cmra_h = get_cameraH(sign_line, horz_line, real_h)

    plt.show()

