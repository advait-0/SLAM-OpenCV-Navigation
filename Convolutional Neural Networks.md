# Convolution
It is the process of multiplying the input matrix by a kernel/filter to give another matrix which has desired characteristics

The following exmple can be used for edge detection where the 3x3 matrix is the kernel
![](https://i.imgur.com/346qixv.png)


![](https://i.imgur.com/cXJ1HMm.png)

The **Padding** of the filter is used around the edges to get optimised outputs

![](https://i.imgur.com/eVREIHf.png)

### Strided convolutions
Are said to be done when the kernel skips some blocks in the input matrix

![](https://i.imgur.com/oKKsrzJ.png)

## Volume convolutions
If we consider a 6x6x3 image to be convolved we can use a 3x3x3 kernel which will convolve it along it's volume. It does so by moving along its cross section and produces a resultant of dimensions 4x4
![](https://i.imgur.com/67vwdDE.png)

### Notations

![](https://i.imgur.com/7g6kHDD.png)


### Max Pooling

![](https://i.imgur.com/M5fWB1W.png)

Max Pooling is the inclusion of the most striking element of the matrix in the final output

An example of a neural network with both convolution and pooling is shown below
![](https://i.imgur.com/xN2Korv.png)


ResNets allow skipping some layers of the neural network

## Transpose Convolution
Allows for getting a bigger output matrix than the input ny multiplying the elements of the two matrices and adding them too in case of an overlap.

![](https://i.imgur.com/uwq6eEA.png)

## U-Net Architecture

![](https://i.imgur.com/t9zaxF0.png)

It works by taking an image applying convolution to it followed by max pooling and more convolutions after which we see a transpose convolution to which we connect a skip connection, then we repeat it till we get a final output with similar dimensions to the input.