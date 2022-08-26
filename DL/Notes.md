## Neural Networks
![Neural network example](NN.png)

 <font size=3> This neural network takes 4 parameters as input and estimates the house price using neurons.</font>

 ## Structured and unstructured data

 <font size=3>Structured: eg. estimating the price of a house using parameters like area, number of rooms (structure members)</font>
 <font size=3>Unstructured: eg. recognizing an image from pixel values. 
 Used in: speech recognition, image recognition,etc</font>

 ## Sigmoid vs RelU
 ![](sig_relu.png)
 <font size=3>Why is sigmoid not preferred?</font>
 <p>The slope the sigmoid function is zero at the start and at the later part of the funtcion. Hence, learning becomes very slow at such points.</p>

 ### In RelU
 <p>In RelU, the gradient of the graph is one.Hence, as compared</p>

 ---
 ## Binary classification
 <font size=3>When categorization is of two types only, either 1 or 0 (true or false)</font>

 ## Logistic regression
 <font size=3>It is an algorithm for binary classification.</font>

## Example
<font size=3>You have to recognize an object either as a cat or non-cat object from an image. (Let the o/p ie. y be 1 in case of a cat and 0 in case of a non-cat) </font>

# Steps:
<font size=3>1. The image is in the form of RGB channel. The pixel values of each channel is stored in a feature vector x. If the image is 64x64 pixels, the total number of elements in the feature vectors will be 64x64x3(Xn).
</font>
<p><font size=3>2. The process takes in (x,y) where x belongs to n; y is either 1 (cat) or 0 (non-cat)</font>
<p><font size=3>The Xn (12288) values of 'input x' are lined up in a column. Suppose, there are m training examples, line up previously made columns side by side to form a matrix of order (Xn)x(m).</font></p>

![Input matrix X](matrices.png)

**The above was the X(input) matrix**

---

<p><font size=3>3. The output ie., 1s and 0s are stored in a matrix Y of 1 row and 'm' columns.</font></p>

![output matrix](output_matrix.png)

**The above is the Y(output) matrix.**

---
---

# Logistic Regression
<p><font size=3>y_hat is the probabilty of output=1 (ie. cat image) given that the input is an image.</font></p>

![y_hat](y_hat.png)

## This is actually the weighted sum.

## Sigmoid function

![sigmoid](sigmoid.png)
<p><font size=3>The sigmoid function is used to return the [weighted sum+bias] as a numner between 1 and 0.</font></p>

<font size=5>Remember: In binary classification, our job is to make the sigmoid funtion return value 1 (and not 0).</font>

<font size=3>In number recognition, it has to be 1 for the correct number while it has to be 0 for the rest. It is the activation number.</font>

# Why cost function?
<font size=3><p>To get the parameters W and b for the weighted sum, we need a cost function.</p></font>

---
---

## Loss function

<font size=3><p>After randomly taking in values for the w and b, we calculate the error in ouputs for the training data is the LOSS FUNCTION.</p></font>

<font size=3><p>Remember: When a cost function is used, it makes gradient descent not work well. </p></font>

### Input and output to the loss function
<font size=3><p>input: ![y_hat](1.png)</p></font>
<font size=3><p>output: 1/2(y-![y_hat](1.png))^2</p></font>


## Cost function: It is a loss function for 'more than one' training examples. AND WE ALWAYS WANT TO MINIMIZE COST: SUM OF SQUARES

![Loss and cost functions](loss_f.png)

---

## Gradient decent
<font size=3><p>The value of the loss/cost function should be minimum. This minimum value occurs for a specific value of w and b. To find these values of w and b(which are the parameters of the cost function), we perform gradient decent.</p></font>

![gradient decent](decent.png)

<font size=3><p>To find the values of w,b for which the cost function is minimum:</p></font>
<font size=3><p>Plot 'cost function' v/s 'w'a and 'b' separately.</p></font>

![W](w_b.png)