# ECE4513 Computer Vision Assignment 2

Tong Zhen 120090694

## Part I Written Exercises

### Problem 1 Lighting (20 points)

![image-20221120005925388](pics\image-20221120005925388.png)

#### A. 

Answer the following regarding the above image (photo credit: ColinBrough from  RGBStock.com). Short answers (several words) are sufficient (8 points):

a. In what direction is the dominant light source: left and above, directly above,  or right and above?

​	right and above, observed from the shadow

b. Why is one of the temple tips (the part that rests on the ear) so bright,  considering that the other tip which has the same material is very dark?

​	By the Lambertian model:

​		Intensity depends on illumination angle. Less light comes in at oblique angles.
$$
I(x) = \rho(x)(\vec{s}\cdot\vec{n(x)})
$$
​		The bright tip is facing to the light source, and reflects light, the angle between s and n is small.

​		The dark tip is reflect light at oblique angles in the Lambertian model.

c. What causes the dark streaks in the wood (in terms of shape, albedo, reflectance,  etc.)?

​	Shape: The wood gap has shape like this: ![image-20221120010804706](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120010804706.png)

​	Albedo: albedo is very small close to 0

​	Reflection: the light cast ito the gap and damped in each reflection, when the light reflect out, its intensity reduced/

d. If the table were completely specular, would the glasses cast a shadow on it  (explain why or why not)?

​	Yes, it will cast a shadow, because the object can reflect the light and cast the light on the region whose light was blocking by the object.

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120011120057.png" alt="image-20221120011120057" style="zoom: 67%;" />

#### B. 

Answer the following using the above illustration. Suppose you have observed the  intensities of three points on an object (𝐼1,𝐼2,𝐼3), which are lit by an infinitely  distant point source (the sun). The surface normal at point 2 is exactly  perpendicular to the sun. The surface normals of points 1 and 3 differ in only one  angle (𝜃), as shown in the cross-section.

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120011204121.png" alt="image-20221120011204121" style="zoom:67%;" />

a. Suppose the surface has a specular component. Will the observed  intensities change as the camera moves (if so why/how)? (4 points)

![image-20221120011446329](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120011446329.png)

b. Suppose the surface material is Lambertian and has uniform (constant)  albedo and that the camera response function is linear (and ignore effects  due to interreflections in the scene). Express the intensities in terms of the  between the surface normal and the lighting direction. Then, show (with  equations for arbitrary observed intensities) how to compute the angles  𝜃12, 𝜃23 between surfaces containing points 1 and 2 and points 2 and 3.  Finally, compute the values of 𝜃12, 𝜃23 for the observed intensities (0.5, 0.9,  0.8). (8 points)

![image-20221120011846345](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120011846345.png)

### Problem 2 Mission Impossible? (10 points)

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120011955084.png" alt="image-20221120011955084" style="zoom:50%;" />

a. A security camera is looking down the hallway at the screen. The camera can  freely rotate but cannot otherwise move. Is it possible to put an image on the  projection screen, such that the screen is undetectable for someone monitoring  the camera? If not, why not? If so, what information is required? (4 points)

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120012112506.png" alt="image-20221120012112506" style="zoom:67%;" />

b. A security guard is sitting behind his desk looking down the hallway. Recently,  while inspecting a pencil, the guard poked his eye, and now he has a patch  covering that eye. But he can still move around and has one good eye. Is it  possible to fool the security guard? If not, why not? If so, what information is  required? (3 points)

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120012135651.png" alt="image-20221120012135651" style="zoom: 67%;" />

c. Is it possible to fool both the security camera and the one-eyed security man at  the same time? If not, why not? If so, what information is required? (3 points)

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120012221943.png" alt="image-20221120012221943" style="zoom:67%;" />

### Problem 3 (10 points)  

As the figure below shows, the Fourier transform of a “tent” function (on the left) is a  squared sinc function (on the right). Advance an argument that shows that the Fourier  transform of a tent function can be obtained from the Fourier transform of a box function.  (Hint: The tent itself can be generated by convolving two equal boxes.)

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120012310539.png" alt="image-20221120012310539" style="zoom:67%;" />

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120012326985.png" alt="image-20221120012326985" style="zoom:50%;" />

### Problem 4 (10 points)  

Images needed to be padded by appending zeros to the ends of rows and columns in the  image (see the following image on the left). Do you think it would make a difference if we centered the image and surrounded it by a border of zeros instead (see image on the right),  but without changing the total number of zeros used? Explain.

![image-20221120012350137](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120012350137.png)

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120012403195.png" alt="image-20221120012403195" style="zoom:67%;" />

### Problem 5 (10 points)  

A continuous Gaussian lowpass filter in the continuous frequency domain has the transfer  function
$$
H(\mu, v) = Ae^{-(\mu^2+v^2)/2\sigma^2}
$$
Show that the corresponding filter in the spatial domain is
$$
h(t, z)=A2\pi \sigma^2e^{-2\pi^2\sigma^2(t^2+z^2)}
$$
![image-20221120012626973](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120012626973.png)

![image-20221120012645793](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120012645793.png)



### Problem 6 (10 points)  

Show that the Fourier transform of the 2-D continuous sine function
$$
f(x, y) = Asin(u_0x + v_0y)
$$
is the pair of conjugate impluses
$$
F(u, v) = -j\frac{A}{2}[\delta(u-\frac{u_0}{2\pi}, v-\frac{v_0}{2\pi})-\delta(u+\frac{u_0}{2\pi},v+\frac{v_0}{2\pi})]
$$
(Hint: Use the continuous version of the Fourier transform and express the sine in terms  of exponentials.)

![image-20221120013541725](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120013541725.png)

![image-20221120013549219](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120013549219.png)

## Part II Programming Exercises

### Problem 1 

**Run**

Library import `matplotlib.pyplot`, `cv2`, `matplotlib.pyplot`

images in relative directory `./images`

```
python main.py
```



### Moire Pattern Suppression in Radiographs (30 points)

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120013658278.png" alt="image-20221120013658278" style="zoom:33%;" />

(a) For each image, apply an N ×N median filter in Problem 1 part (a). Adjust the window size N so that the Moire pattern is removed as much as possible while salient features are properly  preserved. Report your choice of N. Display the filtered image, and comment on the quality of the  filtered image.

N = 5

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120013725828.png" alt="image-20221120013725828" style="zoom: 33%;" /><img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120013738185.png" alt="image-20221120013738185" style="zoom: 33%;" />

N = 10:

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120013844542.png" alt="image-20221120013844542" style="zoom: 33%;" /><img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120013903162.png" alt="image-20221120013903162" style="zoom: 33%;" />

N = 20:

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120014007352.png" alt="image-20221120014007352" style="zoom: 33%;" /><img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120014024487.png" alt="image-20221120014024487" style="zoom: 33%;" />

N = 50:

<img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120014044799.png" alt="image-20221120014044799" style="zoom: 33%;" /><img src="C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120014101248.png" alt="image-20221120014101248" style="zoom: 33%;" />

Picture between 10 to 20 window size is fine. Choose 8 ad 13 for each

![image-20221120014211363](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120014211363.png)

(b) For each image, compute its Discrete Fourier Transform (DFT) (numpy.fft) and display an  image showing the DFT magnitude (numpy.abs). Clearly identify and label the frequency  components that correspond to the Moire pattern.

![image-20221120014517944](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120014517944.png)

The Morie pattern is circled in read

(c) For each image, design a notch filter notchFilter(img, parameter1, …) so that the frequency components for the Moire pattern are suppressed as much as possible while other frequency  components are preserved. Note that the parameters of the function are defined by yourself. Apply  your notch filter to the image’s DFT and display an image showing the filtered DFT magnitude.  Display the filtered image in the spatial domain (numpy.fft). Compare the quality of the result to  that of the filtered image from part (a). (Hint: numpy.meshgrid is useful for creating an (ωx, ωy)  array.)

![image-20221120014622338](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\image-20221120014622338.png)

By taking away the frequency domain Morie pattern and do IFFT, the fine picture appeared.
