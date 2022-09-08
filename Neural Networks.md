# Neural Networks
A neural network can be thought of as a multi-layered function in which the output of the previous layer affects the output of the next layer and this goes on unitl we obtain some final output, which might not be necessarily meaningful at times without modifications

We shall learn more about a neural network by considering a 28x28 grid and finding out how we can determine what number we have as an handwritten input.

## Layers
Layers form the basis of a neural network which can have various factors for differentiation such as detection of a line,loop and so on.The basis of these are entities known as *neurons* 
For the purpose of simplicity they can be considered to hold a value from 0-1.


![](https://i.imgur.com/CP2kLzy.png)

The values assigned can be correlated to the white colour intensity of the each pixel

![](https://i.imgur.com/WBkF9hQ.png)


## Edge detection
To obtain an edge we use the activation values of the neurons along with a weight function which determines their correlation strength with the next layers neuron's.
If for a specific neuron in a specific layer we check for an edge by taking positve weights for the region we are checking for and then negative weights in the surrounding region.

![](https://i.imgur.com/RsiH5HD.png)

So as to *squishify* and get values in the region from 0-1 we use the sigmoid function.
![](https://latex.codecogs.com/png.image?\huge%20\dpi{300}\bg{white}f(x)=\frac{1}{1+e^-x})

or even a ReLu function can be used.

A **Bias** is set which determines the threshold value which the neuron must have to have a meaningful value.

![](https://i.imgur.com/guHkuUJ.png)
<p align = "center">  
Sigmoidal function application
</p>
If we consider a network with 4 layers,
with the outermost being a grid of 28x28 containing 784 pixels and the subsequent layers having 16 neurons and the result being a number from 1-10 we have a possibility for 13,002 connections.


![](https://i.imgur.com/DvvU1LH.png)

## Cost Function
A cost function can be used to check the accuracy of the output of the neural network.
It is the sum of the square of the difference of the final activation value and the desired value (0,1.00)
The higher the cost function is the lesser accuracy the network has in identifying numbers correctly.
The smaller it is the better the accuracy is

Our next objective is to minimize this cost function.
To do this we use the concept of minima
Obtaining a local minima is easy but for a very complex function with so many branches we select a random point a check to it's left and right in 2D 
We shift to the right if the slope of the point is positive or to the left if it's negative. Then we keep checking in the direction of decreasing magnitude of the slope.



![](https://i.imgur.com/7N1xwAu.png)


This logic when applied in 3D space gives us the term *gradient descent*

![](https://i.imgur.com/t3JyijO.png)



## Backpropagation
If we consider an input of 2, the final output won't give us activations only for 2 but for many different values
The activation of 2 should be **increased more** and the activations of others must be **decreased more**

*"We're looking at components which give you the most bang for the buck"*

So we're trying to update the positive weights to give a greater value and the negative to give a lessr value

So we work backwards from our desired output and estimate the values required for the weights and biases of the second to last layer

We get the values for the weights for various different examples and then get their average
![](https://i.imgur.com/14w41as.png)

But going through all data is a computational challenge so we randomly divide this data in mini batches and then make these adjustments
This is the **Stochastic gradient descent**

