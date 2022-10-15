# HM1 Report

TONG ZHEN 120090694

---

- **Question 1**
    
    **Q:** Show that forming unweighted local averages, which yields an operation of the form
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled.png)
    
    is a convolution. What is the kernel of this convolution?
    
    **A:**
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled.jpeg)
    
- **Question 2**
    
    **Q:** Write E0 for an image that consists of all zeros with a single one at the center. Show that convolving this image with the kernel
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%201.png)
    
    (which is a discretized Gaussian) yields a circularly symmetric fuzzy blob.
    
    **A:**
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%201.jpeg)
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%202.png)
    
    The *symmetric Gaussian kernel* yields a symmetric fuzzy blob.
    
- **Question 3**
    
    **Q:** Show that convolving a function with a δ function simply reproduces the original function. Now show that convolving a function with a shifted δ function shifts the function.
    
    **A:**
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%202.jpeg)
    
- **Question 4**
    
    **Q:** Derive the perspective equation projections for a virtual image located at a distance ${f}^\prime$ in front of the pinhole.
    
    **A:**
    
    The perspective projection equations are derived in this section from the collinearity of the point $P$, its image $p$, and the pinhole $O$. We set the pinhole $O$ to be the origin, the $k$ axis to be perpendicular to the image graph.
    
    Let $P$ denote a scene point with coordinates $(X,Y,Z)$ and p denote its image with coordinates $(x, y, z) \ and \ d = -f^\prime$. 
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%203.jpeg)
    
- **Question 5**
    
    Derive the thin lens equation.
    
    Hint: consider a ray $r_0$ passing through the point P and construct the rays $r_1$ and $r_2$ obtained respectively by the refraction of $r_0$ by the right boundary of the lens and the refraction of $r_1$ by its left boundary.
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%204.jpeg)
    
- **Question 6**
    
    **Q:** Give a geometric construction of the image P` of a point P given the two focal point F and F` of a thin lens.
    
    **A:**
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%205.jpeg)
    
- **Question 7**
    
    **Q:** Let $O$ denote the homogeneous coordinate vector of the optical center of a camera in some reference frame, and let $M$ demote the corresponding perspective projection matrix. Show that $MO = 0$
    
    **A:**
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%206.jpeg)
    
- **Question 8**
    
    **Q:**
    
    Show that when the camera coordinate system is skewed and the angle $\theta$ between the two image axes is not equal to 90 degrees, then EP. (2.11) transforms into Eq. (2.12)
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%203.png)
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%204.png)
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%205.png)
    
    **A:**
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%207.jpeg)
    
- **Question 9**
    
    **Q:** Write formulas for the matrices $_B^AR$ in Eq. (1.8) when (B) is deduced from (A) via a rotation of angle θ about the axes $\vec{i_A}$, $\vec{j_A}$,and $\vec{k_A}$ respectively.
    
    **A:**
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%208.jpeg)
    
- **Question 10**
    
    **Q:** Show that rotation matrices are characterized by the following properties:
    
    (a) the inverse of a rotation matrix is its transpose
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%209.jpeg)
    
    (b) its determinant is 1
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%2010.jpeg)
    

## Part II Programming Exercises

visit: [https://github.com/58191554/Computer_Vision_longda/tree/main/HM_1](https://github.com/58191554/Computer_Vision_longda/tree/main/HM_1) 

Environment: python 3.7+

library: numpy, matplotlib

Two python file :

problem a, b, c: [getVanishingPoint.py](http://getVanishingPoint.py) 

problem d: [getHeight.py](http://getHeight.py) 

### Problem 1 Single-View Metrology

- **Problem a**
    
    In the first program set `manual = True` , if you want to select the parallel line by hand.
    
    ```python
    vps = getVanishingPoint(im, **manul=True**)
    ```
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%206.png)
    
    Specify the $VPs (u, v)$ and plot the $VPs$ and the lines used to estimate them on the image plane. The two parallel line are:
    
    $l_1 = a_1x + b_1y + c_1$
    
    $l_2 = a_2x + b_2y + c_2$
    
    the cross point $(x_1, x_2)$is:
    
    $[\begin{matrix} a_1 & b_1 \\ a_2 & b_2 \end{matrix}] [\begin{matrix} x_1\\ x_2 \end{matrix}] = [\begin{matrix} c_1\\ c_2 \end{matrix}]$
    
    therefore $[\begin{matrix} x_1\\ x_2 \end{matrix}] = A^{-1}c$
    
    Plot the ground horizon line and specify its parameters in the form $au + bv + c = 0$. 
    
    By cross product of the two points $\vec{p}, \vec{q}$, we can get the line
    
    $\vec {p} \times \vec{q} = \vec{l}$
    
    Normalize the parameters so that: $a^2 + b^2 = 1$:
    
    k = $\sqrt{a^2 + b^2}$
    
    $l:\tilde{a}x + \tilde{b}y + \tilde{c} = \frac{a}{k}x + \frac{b}{k}y + \frac{c}{k} = 0$
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%207.png)
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%208.png)
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%209.png)
    
- **Problem b**
    
    Use the fact that the vanishing points are in orthogonal directions to estimate the camera focal length (f) and optical center (u0, v0). 
    
    Our assumption on K: unit aspect ratio & no skew
    
    $K = [\begin{matrix} f & 0 & u_0 \\ 0 & f & v_0 \\ 0 & 0 & 1 \end{matrix}
    \quad]$
    
    We use the orthogonality of $V_1, V_2, V_3$
    
    $V_i=\lambda _{i}\left[ u_{i},V_{i},1\right] ^{T}$
    
    $\left( K^{-1}V_{1}\right) ^{T}\left( K^{-1}V_{2}\right) =\left( K^{-1}V_{1}\right) ^{T}\left( K^{-1}V_{3}\right) =\left( K^{-1}V_{3}\right) ^{T}\left( K^{-1}V_{2}\right) =$0
    
    $K^{-T}K^{-1} = [\begin{matrix} 1/f^2 & 0 & -u_0/f^2 \\  0 & 1/f^2 & -v_0/f^2 \\ -u_0/f^2 & -v_0/f^2 & u_0^2/f^2+v_0^2/f^2+ +1 \end{matrix}]  = [\begin{matrix} b1 & 0 & b2 \\ 0 & b1 & b3 \\ b2 & b3 & b4 
     \end{matrix}]$
    
    $[\begin{matrix} u1*u2+v1*v2 & u1+u2 & v1+v2 & 1 \\
    u3*u2+v3*v2 & u3+u2 & v3+v2 & 1 \\
    u1*u3+v1*v3 & u1+u3 & v1+v3 & 1 \\\end{matrix}][\begin{matrix} b1 \\ b2 \\ b3 \\ b4 \end{matrix}] = \bold0$
    
    In `get_intrinsic()`, we solve the $Ab = 0$ using the least square method.
    
    $b$ is the eigenvector of the smallest $A^TA$ eigenvalue
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%2010.png)
    
- **Problem c**
    
    Show how to compute the camera’s rotation matrix when provided with vanishing points in the X, Y, and Z directions
    
    in function `get_rotationM` 
    
    We solve the rotation matrix by:
    
    $[V_1, V_2, V_3] = K(R|t)(\begin{matrix} 1 & 0 & 0\\ 0 & 1 & 0 \\ 0&0&1\\0&0&0\end{matrix})$
    
    $r_i = \frac{K^{-1}v_i}{||K^{-1}v_i||}$
    
    ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%2011.png)
    
- **Problem d**
    
    We need to assume that the height line we draw are parallel to the vertical z axis in the world corrdinate (W)
    
    - Turn in an illustration that shows the horizon line, and the lines and measurements used to estimate the heights of the building, tractor, and camera.
    1. We first get the vanishing points and vanishing line in the picture
    2. Connect the bottom of the sign and the bottom of the object $M$to be estimated, the top of the object is $N$
    3. Extend the line and intersect with the vanishing line, get point $P$
    4. Connect the point $P$ and the top of the sigh, intersect the vertical line of the object to be estimated at $Q$.
    5. $H = H_{sign}\frac{|MN|}{|MQ|}$ 
        
        ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%2011.jpeg)
        
    - Report the estimated heights of the building, tractor, and camera.
    1. Extend the line of the sign and intersect with the vanishing line, get point $R$. Denote the bottem of the sign is $S$, top is $T$
    2. The height of the camera is $H = H_{sign}\frac{|SR|}{|ST|}$
        
        ![Untitled](HM1%20Report%20f8b9b78a4205490a81d032dcd8f13ff5/Untitled%2012.png)