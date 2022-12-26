# Assignment 3 

Tong Zhen 120090694

#### Part I Written Exercise

##### Q1:

Show that forming unweighted local averages, which yields an operation of the form

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221220151456455.png" alt="image-20221220151456455" style="zoom:45%;" />

is a convolution. What is the kernel of this convolution?

##### A1:

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221220151530789.png" alt="image-20221220151530789" style="zoom:37%;" />

##### Q2:

Each pixel value in 500×500 pixel image I is an independent, normally distributed random  variable with zero mean and standard deviation one. I is convolved with the (2k + 1) × (2k + 1)  kernel G. What is the covariance of pixel values in the result? There are two ways to do this;  on a case-by-case basis (e.g., at points that are greater than 2k + 1 apart in either the x or y direction, the values are clearly independent) or in one fell swoop. Don’t worry about the pixel  values at the boundary.

##### A2:

![image-20221220153312120](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221220153312120.png)

#### Part II Programming Exercises

##### Problem 1 

**Image Pyramid (20 points)** 

###### (a) 

Display a Gaussian and Laplacian pyramid of level 5 (using your code). It should be  formatted similar to the figure below.

| Parameter      | Value |
| -------------- | ----- |
| Kernel size    | 11x11 |
| Gaussian Sigma | 0.8   |

First, do Gaussian Convolution to the image and down sample, here use nearest neighbor down sample. Iterate for 5 times.

Gaussian Pyramid

![image-20221220202725313](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221220202725313.png)

Do the up sample for g5, and get 
$$
e_4 = expand(g_5) \\
l_4 = g_4-e_4
$$
 Iterate Laplacian until we get l0

Laplacian Pyramid![image-20221220202738915](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221220202738915.png)

###### (b) 

Display the FFT amplitudes of your Gaussian/Laplacian pyramids. Appropriate display  ranges should be chosen so that the changes in frequency in different levels of the pyramid are  clearly visible. Explain what the Laplacian and Gaussian pyramids are doing in terms of  frequency.

![Gaussain Fourier0](D:\Courses_2022_Fall\ECE4513\HM3\prob_1\Gaussain Fourier0.jpg)

![Gaussain Fourier1](D:\Courses_2022_Fall\ECE4513\HM3\prob_1\Gaussain Fourier1.jpg)

![Gaussain Fourier2](D:\Courses_2022_Fall\ECE4513\HM3\prob_1\Gaussain Fourier2.jpg)

![Gaussain Fourier3](D:\Courses_2022_Fall\ECE4513\HM3\prob_1\Gaussain Fourier3.jpg)

![Gaussain Fourier4](D:\Courses_2022_Fall\ECE4513\HM3\prob_1\Gaussain Fourier4.jpg)

![Gaussain Fourier5](D:\Courses_2022_Fall\ECE4513\HM3\prob_1\Gaussain Fourier5.jpg)

![Laplacian Fourier0](D:\Courses_2022_Fall\ECE4513\HM3\prob_1\Laplacian Fourier0.jpg)

![Laplacian Fourier1](D:\Courses_2022_Fall\ECE4513\HM3\prob_1\Laplacian Fourier1.jpg)

![Laplacian Fourier2](D:\Courses_2022_Fall\ECE4513\HM3\prob_1\Laplacian Fourier2.jpg)

![Laplacian Fourier3](D:\Courses_2022_Fall\ECE4513\HM3\prob_1\Laplacian Fourier3.jpg)

![Laplacian Fourier4](D:\Courses_2022_Fall\ECE4513\HM3\prob_1\Laplacian Fourier4.jpg)

The Gaussian Pyramid can keep the low frequency information and the Laplacian Pyramid keep the high frequency inforation

##### Problem 2 

**Edge Detection (20 points)**

###### (a)

Build a simple gradient-based edge detector that includes the following functions `gradientMagnitude` & `edgeGradient`:

![image-20221221232057714](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221221232057714.png)

do the non-max-suppression

![image-20221222095112354](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221222095112354.png)

Double threshold

| Parameter            | Value |
| -------------------- | ----- |
| low Threshold Ratio  | 0.05  |
| high Threshold Ratio | 0.2   |
| weak value           | 100   |
| strong value         | 255   |

![image-20221222101032801](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221222101032801.png)

Edge Tracking by Hysteresis

![image-20221222101113814](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221222101113814.png)

Run

```
python edge_detector.py task_a
```

![image-20221223223359437](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221223223359437.png)

You will find the output under the **prob_2\data\png\test**

Run BSDS 500 boundary prediction evaluation suite

[berkeley.edu/Research/Projects/CS/vision/bsds/](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/)

put the output of `data/images/test` pictures under `data/png/test`

Compile the extension module in the src directory.

```shell
python setup.py build_ext --inplace
python verify.py <path_to_bsds500_root_directory>
```

It gains 0.848485 precision.

![image-20221223185747820](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221223185747820.png)

| Average | Value    | Overall | Value    |
| ------- | -------- | ------- | -------- |
| f1      | 0.747495 | f1      | 0.704546 |
| f2      | 0.746673 | f2      | 0.599604 |
| f3      | 0.639921 | f3      | 0.548863 |
| f4      | 0.633149 | f4      | 0.548913 |
| f5      | 0.839334 | f5      | 0.429897 |

precision: 0.848485

f1: 0.704546

best precision: .908492

best f1: 0.708547

###### (b)

Sobel-like kernels are used to calculate the derivative in other direction

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221223183611060.png" alt="image-20221223183611060" style="zoom:50%;" />
$$
I_i = F_i*I, i\in[1, 2, 3, 4]\\
magnitude = max(I_1, I_2, I_3, I_4)
$$
The theta is estimated by the largest value in the eight direction.
$$
theta\_index = argmax(I_1,I_2,I_3,I_4,-I_1,-I_2,-I_3,-I_4) \\
theta = \frac{theta\_index}{8}\cdot \frac{\pi}{4}
$$
**Qualitative results:**

<img src="D:\Courses_2022_Fall\ECE4513\HM3\prob_2\data\images\test\3063.jpg" alt="3063" style="zoom: 67%;" /><img src="D:\Courses_2022_Fall\ECE4513\HM3\prob_2\data\png\test\3063.png" alt="3063" style="zoom: 67%;" />

<img src="D:\Courses_2022_Fall\ECE4513\HM3\prob_2\data\images\test\5096.jpg" alt="5096" style="zoom: 67%;" /><img src="D:\Courses_2022_Fall\ECE4513\HM3\prob_2\data\png\test\5096.png" alt="5096" style="zoom: 67%;" />

Run

```
python edge_detector.py task_b
```

You will find the output under the prob_2\data\png\test

![image-20221223223221007](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221223223221007.png)

Run the verify.py as (a) above

![image-20221223222152732](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221223222152732.png)

| Overall | Value    | Average | Value    |
| ------- | -------- | ------- | -------- |
| f1      | 0.704653 | f1      | 0.747795 |
| f2      | 0.599594 | f2      | 0.746455 |
| f3      | 0.548953 | f3      | 0.639835 |
| f4      | 0.548881 | f4      | 0.633149 |
| f5      | 0.429855 | f5      | 0.839537 |

precision: 0.848883

f1: 0.704653

best precision: .908969

best f1: 0.708595

##### Problem 3 

**Feature Tracker (40 points)**

###### (a)

pseudocode

```pseudocode
input image

get sobelx and sobelx from convolution image with Sobel filter
get Ixx, Ixy, Iyy from sobelx and sobelx
do the Gaussain Blur of Ixx, Ixy, Iyy
set a in [0.01, 0.06]
get determinant:detM = Ixx * Iyy - Ixy *Ixy
get trace: traceM = Ixx + Iyy
get response: response = detM - a * traceM *traceM
for element in response matrix{
	do threshold selection: element value > -tau && element value<tau
	do non-max-suppress: check element is the max in its 5x5 patch
}for end

for element in response matrix{
	if(element value > 0){
		add element position to keyXs, keyYs
	}
}for end

output keyXs, keyYs collection
```

hyperparameter used:
$$
\tau = 10^7, a = 0.05
$$
patch  size used in non max suppression:
$$
patch\_size = 5\times5
$$
Harris key point:

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221223224355922.png" alt="image-20221223224355922" style="zoom:50%;" /><img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221223221946836.png" alt="image-20221223221946836" style="zoom:50%;" />

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221223224405974.png" alt="image-20221223224405974" style="zoom:50%;" />

###### (b)

Transition formula:

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221224014127084.png" alt="image-20221224014127084" style="zoom:53%;" />

pseudocode

```pseudocode
input Harris Corner points position x, y, cur_image, and next_image

do the Gaussain Blur for the cur_image, and next_image
get Ix and Iy by convolution the cur_image with sobel filter
initialize next_x, and next_y as x and y
get intensity patch I_xyt centered at x, y in image

while (find convergence less than maximen time){
	if the next_x or next_y out of image{
		output next_, next_y
	}
	get interpolation for image patch centered at next_x, and next_y
	do intensity difference: I_next_xy - I_xyt
	solve Ax=b in (Transition formula)
	update next_x += x[0]
	update next_y += x[1]
}
```

hyperparameter used:
$$
window \ size: W_{size} = 15\\
Iteration\ max = 30\\
stop\ threshold:|(u, v)|_2 <= 0.01
$$




The green points are the corner points, the red points are the track trajectories for 50 steps, and the blue points are the points out of the boundary.

200 points to track![200track](D:\Courses_2022_Fall\ECE4513\HM3\prob_3\200track.jpg)

20 points to track

![20track](D:\Courses_2022_Fall\ECE4513\HM3\prob_3\20track.jpg)

**Run**

input the numbers of points you want to track after the python file.

```
python FeatureTracker.py 20
```

![image-20221224010410595](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221224010410595.png)

It will generate a file with track points number as name, like `20track.jpg`
