# Football Analysis Project

## Introduction
The goal of this project is to detect and track players, referees, and footballs in a video using YOLO, one of the best AI object detection models available. We will also train the model to improve its performance. Additionally, we will assign players to teams based on the colors of their t-shirts using Kmeans for pixel segmentation and clustering. With this information, we can measure a team's ball acquisition percentage in a match. We will also use optical flow to measure camera movement between frames, enabling us to accurately measure a player's movement. Furthermore, we will implement perspective transformation to represent the scene's depth and perspective, allowing us to measure a player's movement in meters rather than pixels. Finally, we will calculate a player's speed and the distance covered. This project covers various concepts and addresses real-world problems, making it suitable for both beginners and experienced machine learning engineers.


## Steps

1. Install the library within the project directory by following command. 
 ```pip install ultralytics```

2. Add the input video in the **input_video** folder.

3. Write the object detection code by creating a **yolo_inference.py** file with project directory. And run the file. 

4. Create a new file **football_training_yolo_v5.ipynb** for downloading the data set from *roboflow*. And run the file.

5. And for training the model use COLAB, later then download and add the model into *Models* folder