# Traffic Sign Classifier using CNN and Keras (Pyhton) - Algorithm development and Testing using 50,000 images

CNN classifier is trained using traffic sign images taken from he German Traffic Sign Benchmark is a multi-class, single-image classification challenge held at the International Joint Conference on Neural Networks (IJCNN) 2011.

The dataset used in the work is not uploaded in repository due to large size of file and hence can be provided on request.

The datset contains traffic sign images each with size 32 x 32 x 3 (channel) i.e RGB
Training images = 34799
Validation images = 4410
test images = 12630

## Ouput Labels (categories): 43
Details are as:
* ( 0, b'Speed limit (20km/h)')
* ( 1, b'Speed limit (30km/h)')
* ( 2, b'Speed limit (50km/h)')
* ( 3, b'Speed limit (60km/h)')
* ( 4, b'Speed limit (70km/h)')
* ( 5, b'Speed limit (80km/h)')
* ( 6, b'End of speed limit (80km/h)')
* ( 7, b'Speed limit (100km/h)')
* ( 8, b'Speed limit (120km/h)')
* ( 9, b'No passing')
* (10, b'No passing for vehicles over 3.5 metric tons')
* (11, b'Right-of-way at the next intersection')
* (12, b'Priority road')
* (13, b'Yield')
* (14, b'Stop')
* (15, b'No vehicles')
* (16, b'Vehicles over 3.5 metric tons prohibited')
* (17, b'No entry')
* (18, b'General caution')
* (19, b'Dangerous curve to the left')
* (20, b'Dangerous curve to the right')
* (21, b'Double curve')
* (22, b'Bumpy road')
* (23, b'Slippery road')
* (24, b'Road narrows on the right')
* (25, b'Road work')
* (26, b'Traffic signals')
* (27, b'Pedestrians')
* (28, b'Children crossing')
* (29, b'Bicycles crossing')
* (30, b'Beware of ice/snow')
* (31, b'Wild animals crossing')
* (32, b'End of all speed and passing limits')
* (33, b'Turn right ahead')
* (34, b'Turn left ahead')
* (35, b'Ahead only')
* (36, b'Go straight or right')
* (37, b'Go straight or left')
* (38, b'Keep right')
* (39, b'Keep left')
* (40, b'Roundabout mandatory')
* (41, b'End of no passing')
* (42, b'End of no passing by vehicles over 3.5 metric tons')

NOTE: The dataset is zipped and then uploaded to repository. Hence after download, unzip the data and then add it 
to the working directory and then run the python algorithm for classfication.

## Folder details:
* Traffic sign classifier.py - algorithm
* train.p.zip - train dataset of images (not in repo)
* test.p.zip - test dataset of images (not in repo)
* valid.p.zip - validation dataset of images (not in repo)


## References:
[German Traffic Sign Benchmark](http://benchmark.ini.rub.de/)














