## Binary Classification
It tells us about the output which is either a cat or non-cat image after it takes in out input vector X which is a 64x64x3 dimensional vector containing RGB data value of the grid cells. The network has to process this data and give an output

![](https://i.imgur.com/oTYK0Es.png)

### Notations

![](https://i.imgur.com/BAu12NJ.png)

In (x,y) x represents the input matrix data which is a Vector with dimensions nx
y is the output which is (0,1) cat or no cat and the data set is represented by X.

![](https://i.imgur.com/6l7Rhi1.png)
![](https://latex.codecogs.com/svg.image?\hat{y}) here represents the possibility of getting a 1(cat) in the dataset of x containing parameters w and b, to get output between 0 and 1 the *sigmoid squishification function* is being used here

A loss function is used to tell how well the accuracy of the output is,
Cost function is the loss function averaged over all the dataset and how well w and b are doing for the dataset
![](https://i.imgur.com/QEYe1Vz.png)

Gradient decent used to find global minima to find minimum value of cost function for maximum accuracy.
![](https://i.imgur.com/R390PZu.png)


![](https://i.imgur.com/AKDPHQ0.png)

![](https://i.imgur.com/sZzlnbZ.png)


## Vectorization
Neural networks can be implemented with the help of for loops as well as by vectorization and using numpy libraries, if we see the calculation times of these we see that vectorization increases the processing speeds by more than 300 times.


![](https://i.imgur.com/GtfAIkx.png)

![](https://i.imgur.com/eRigkw8.png)


Intuitively logistic regression function is derived from the probability of getting 1( y hat) as the output.
![](https://i.imgur.com/V17L9GD.png)
