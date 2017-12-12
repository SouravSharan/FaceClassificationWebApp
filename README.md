# FaceClassificationWebApp

Face It is a simple Web Application, which when given an image, is able to detect a face (show with a boundary box) and give a result saying whether **Narendra Modi** and/or **Arvind Kejriwal** are present in the image or not. </br>

[The project is available here](https://0ca63b28.ngrok.io/)

<img src="https://github.com/SouravSharan/FaceClassificationWebApp/blob/master/demo/Screenshot_2017-12-11-21-44-47-093_com.android.chrome.png" height=500> <img src="https://github.com/SouravSharan/FaceClassificationWebApp/blob/master/demo/Screenshot_2017-12-11-21-44-17-681_com.android.chrome.png" height=500> <img src="https://github.com/SouravSharan/FaceClassificationWebApp/blob/master/demo/Screenshot_2017-12-11-21-43-50-915_com.android.chrome.png" height=500> 

## Tech Stack
  * OpenCV
  * Keras
  * Flask
  * HTML, CSS, Bootstrap
  * Beautiful Soup

## Face Detection and Classification
  Data was collected by scraping images from google using Beautiful Soup.

## Face Detection and Classification
  Several approches were tried for face classification. 
  * **Convolutional neural network** </br>
    Even though training accuracy was high, the model didn't work well on test set, probably due to less data.
  * **OpenCV_contrib face detection** </br>
    OpenCV has 3 face recognition techniques: </br>
      * Eigen Faces
      * Fisher Faces
      * Local Binary Pattern Histograms (LBPH) </br>
    LBPH gave the highest accuracy on the dataset.
     
## Website
  The website is mobile friendly. It has a Flask backend and is  hosted on AWS https://0ca63b28.ngrok.io. 
