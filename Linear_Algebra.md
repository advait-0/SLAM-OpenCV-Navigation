# Linear Algebra

## Vectors

So understanding Linear Algebra begins with the understanding of Vectors.

Vectors are points in 2D or 3D space having magnitude and direction

<img src="file:///run/user/1000/doc/fce6f523/Vectors.png" title="Vectors" alt="Vectors" data-align="center">

The interpretation and usage of Vectors as they are varies in various fields

- Computer Science enthusiasts perceive them as a list of numbers.

- Physicists perceive them as a quantity with magnitude and direction

- Mathematicians thinks of it as a combination of both and something on which operations can be performed.

#### Representation of Vector

![](https://latex.codecogs.com/svg.image?\huge%20\hat{i})   (pronounced i cap or i hat) is the representation of the unit vector along the standard X-axis

![](https://latex.codecogs.com/svg.image?\huge%20\hat{j}) (pronounced j cap or j hat) is the representation of the unit vector along the standard Y-axis

![](https://latex.codecogs.com/svg.image?\huge%20\hat{k}) (pronounced k cap or k hat) is the representation of the unit vector along the standard Z-axis

Together these three vectors are known as the **Basis Vectors** and the transformations and operations applied to these three give birth to Linear Algebra

![](https://latex.codecogs.com/svg.image?\huge%20\begin{bmatrix}%20x\\%20y\\z\end{bmatrix})

This is the standard representation of a 3D Vector in Matrix form with x, y and z representating the x,y and z coordinates in space respectively.

*Span* for 2D vectors is defined as all of the possible region which all the possible combinations of the two vectors can cover, this usually gives us a planar surface.

For 3D vectors span usually gives the volume which all possible vector combinations can cover. 

## Linear Transformations

Defined as rotation and shearing of the principle axes which contain the basis vectors

It must satisfy two conditions:

- Lines must remain lines without bending

- Origin must remain fixed

<img src="https://i.imgur.com/V6Rumd5.png" title="Rotation transformation" alt="Rotation transformation" data-align="center">

<p align = "center">  
Rotation Transformation  
</p>



In this Example the basis vectors are rotated 90&deg; counterclockwise

The first matrix is the matrix representing the transformation of the basis vectors any given matrix with given vector coordinates can be multiplied with this to obtain the resultant vector coordinates



<img src="https://i.imgur.com/eKTXT8D.png" title="" alt="" data-align="center">

<p align = "center">  
Shear Transformation 
</p>

This can be algebraically represented as

<img src="https://i.imgur.com/CauHtJS.png" title="" alt="" data-align="center">

### Matrix Multiplication

Matrix multiplication can be visualized as the combination of two separate transformations

It is analogous to writing  ![](https://latex.codecogs.com/svg.image?f(g(x)))  

The above-mentioned *rotation* and *shear* transformation matrices can be written as a single composition matrix by multiplying the two of them together numerically.



![](https://latex.codecogs.com/svg.image?\huge%20\begin{bmatrix}%200&%20-1%20\\%201&%200%20\\\end{bmatrix}\begin{bmatrix}1%20&3%20%20\\%202&1%20%20\\\end{bmatrix}%20=%20\begin{bmatrix}0*1+(-1*2)%20&%20%20%200*3+(-1*1)%20%20\\1*1+0*2%20&1*3+0*1%20%20\\\end{bmatrix})



This gives us the compositon matrix

![](https://latex.codecogs.com/svg.image?\huge%20\begin{bmatrix}%20-2&%20-1%20\\%201&%203%20\\\end{bmatrix})

Any given vector matrix multiplied to this matrix will give the product vector which has been both rotated as well as sheared.

General matrix multiplication formulae:

<img src="https://i.imgur.com/omgW8h3.png" title="Matrix Multiplication" alt="" data-align="center">

Another thing to note is that

![](https://latex.codecogs.com/svg.image?\huge%20M_1.M_2%20\neq%20M_2.M_1)

Although,

![](https://latex.codecogs.com/svg.image?\huge%20(AB)C=A(BC))

This is all applicable for 3D transformations as well

### Determinant

The factor by which a linear transformation changes any area(in 2D space) or volume(in 3D space) is known as the Determinant

The basis "1" here being the area or volume of basis vectors.

<img src="https://i.imgur.com/ZTIIdTm.png" title="" alt="" data-align="center">



<p align = "center">  
Determinant of a 2x2 Matrix
</p>

The determinant of a 2D or 3D matrices being zero signifies that the matrix has lost one or more of its dimensions thereby giving an area or volume of zero

<img src="https://i.imgur.com/RClGZDF.png" title="" alt="" data-align="center">

The negative of a determinant signifies the flipping of orientation

<img src="https://thumbs.gfycat.com/FrighteningWelloffAsiantrumpetfish-size_restricted.gif" title="" alt="" data-align="center">

For 3D Matrices this can be understood on the basis of the right hand rule, if you can still use the right hand to denote the original axes after transformation, the determinant is positive or else it's negative.



Notations to solve 2D determinant:

<img src="https://i.imgur.com/qPGJPfa.png" title="" alt="" data-align="center">

To solve 3D Determinant:
<img src="https://i.imgur.com/NV6hvmw.png" title="" alt="" data-align="center">

### Linear System of Equations

Linear systems of equations can be solved using matrices

wherein the coefficients of the variables can be assumed to be a transformation matrix and the variables as a vector to which the transformation is being applied, the constant of such equations give us the resultant vectors.

![]![](https://latex.codecogs.com/svg.image?\huge%20\\2x+5y+3z=-3\\4x+0y+8z=0\\1x+3y+0z=2\\)

The given equations can be represented as:

![](https://latex.codecogs.com/svg.image?\huge%20\begin{bmatrix}2%20&5%20%20&3%20%20\\%204&%200%20&%208%20\\1%20&%203%20&%200%20\\\end{bmatrix}\begin{bmatrix}x%20\\y%20\\z\end{bmatrix}%20=%20\begin{bmatrix}-3%20\\0%20\\2\end{bmatrix})

To obtain the values of x,y and z we use the concept of inverse which essentially reverses the change produced by the transformation matrix. The resultant obtained by multiplying a matrix by its inverse gives us no net change, which can also be denoted by a unit matrix having same order as the transformation matrix

![](https://latex.codecogs.com/svg.image?\huge%20A^{-1}A\overrightarrow{x}=A^{-1}\overrightarrow{v})

![](https://latex.codecogs.com/svg.image?\huge%20\overrightarrow{x}=A^{-1}\overrightarrow{v})



**Rank** of a matrix is defined as the number of dimensions in the output of a transformation

<iframe src='https://gfycat.com/ifr/CleanDisloyalFishingcat' frameborder='0' scrolling='no' allowfullscreen width='640' height='404'></iframe>

<iframe src='https://gfycat.com/ifr/CleanDisloyalFishingcat' frameborder='0' scr
olling='no' allowfullscreen width='640' height='404'></iframe>

<img src="https://thumbs.gfycat.com/LimpingMasculineGermanshepherd-size_restricted.gif" title="" alt="" data-align="center">

Column space is a term used to define the number of dimensions in the column span

if the number of columns are equal to the rank the matrix is said to be *full rank*

### Dot Product

Dot product of two vectors is the multiplication of the projection of one vector 1 on vector 2 with vector 2, the vice-versa also hold true.

<img src="https://thumbs.gfycat.com/FrailPastelIndianhare-size_restricted.gif" title="" alt="Dot product" data-align="center">

<p align = "center">  
Dot Product
</p>

### Cross Product

Cross product gives us a third vector mutually perpendicular to the first two vectors the magnitude of which gives us the area of the parallelegram bounded by the two initial vectors

![](https://s4.gifyu.com/images/2022-08-20-01-40-34.gif)

The direction of which is found by the right hand rule

Cross product is computed by:

![](https://i.imgur.com/OWEoVjW.png)

#### Change of Basis

This can be done when the basis vectors are being interpreted differently, so as to obtain some standard result

Usually done using abovementioned linear transformation methods

### Eigenvectors and Eigenvalues

During a linear transformation if a vector doesn't rotate and travels only along it's span, it's called an eigenvector and the factor by which its dimensions change is called their eigenvalue
