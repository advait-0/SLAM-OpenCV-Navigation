
![](https://i.imgur.com/kaTAvLg.png)

### Sliding window detection
This can be done by sliding a frame over the image and it wouuld check for the object in that particular window.
But this method is computationally expensive

### Bounding Box predictions

![](https://i.imgur.com/ylDEO2l.png)

A small frame is selected within an image, an 8 dimensional vector is then created which contains information from up to down as [0, bx, by, bh, bw, c1, c2, c3]. The zero here specifies that it contains an object of interest, bx is the coordinate of the centroid of the object of interest in the frame, by is same as bx but for y coordinate. bh and bw are coordinates of the edge of the red box showing the ROI. c1,c2 and c3 specify the type of object in the frame eg a car, bus etc.

### Intersection over union
If two bounding boxes overlap the correct bounded region would be the one with intersection of union >=0.5 where iou is the ratio of area of the intersection to the area of union.
![](https://i.imgur.com/2cjgual.png)

### Non Max Suppression
Keeps the boxes with higher probability of containing the object and suppresses the rest.
![](https://i.imgur.com/IfxXq9C.png)

#### Anchor Boxes
Used to overcome the problem of grid overlaps, not usually an issue when using large grids