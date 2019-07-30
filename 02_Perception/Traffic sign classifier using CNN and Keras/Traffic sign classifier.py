'''
Developer: M.Sc. Shiva Agrawal
Place: Germany
Version: 1.0
Date: 09.07.2019
Description:  Traffic sign classifier using CNN and Keras

the dataset is available in form of .p files.
train.p, test.p and valid.p
It is taken from The German Traffic Sign Benchmark is a multi-class, single-image classification challenge
held at the International Joint Conference on Neural Networks (IJCNN) 2011.

the datset contains traffic sign images each with size 32 x 32 x 3 (channel) i.e RGB
Training images = 34799
Validation images = 4410
test images = 12630

Ouput Labels (categories): 43
------------------------------
Details are as:
( 0, b'Speed limit (20km/h)')
( 1, b'Speed limit (30km/h)')
( 2, b'Speed limit (50km/h)')
( 3, b'Speed limit (60km/h)')
( 4, b'Speed limit (70km/h)')
( 5, b'Speed limit (80km/h)')
( 6, b'End of speed limit (80km/h)')
( 7, b'Speed limit (100km/h)')
( 8, b'Speed limit (120km/h)')
( 9, b'No passing')
(10, b'No passing for vehicles over 3.5 metric tons')
(11, b'Right-of-way at the next intersection')
(12, b'Priority road')
(13, b'Yield')
(14, b'Stop')
(15, b'No vehicles')
(16, b'Vehicles over 3.5 metric tons prohibited')
(17, b'No entry')
(18, b'General caution')
(19, b'Dangerous curve to the left')
(20, b'Dangerous curve to the right')
(21, b'Double curve')
(22, b'Bumpy road')
(23, b'Slippery road')
(24, b'Road narrows on the right')
(25, b'Road work')
(26, b'Traffic signals')
(27, b'Pedestrians')
(28, b'Children crossing')
(29, b'Bicycles crossing')
(30, b'Beware of ice/snow')
(31, b'Wild animals crossing')
(32, b'End of all speed and passing limits')
(33, b'Turn right ahead')
(34, b'Turn left ahead')
(35, b'Ahead only')
(36, b'Go straight or right')
(37, b'Go straight or left')
(38, b'Keep right')
(39, b'Keep left')
(40, b'Roundabout mandatory')
(41, b'End of no passing')
(42, b'End of no passing by vehicles over 3.5 metric tons')

'''

import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

# for CNN model development and optimization using keras
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Dense,Flatten,Dropout
from keras.optimizers import Adam

## load the dataset from .p files into Python using pickle
with open('./train.p',mode='rb') as training_data:
    train = pickle.load(training_data)

with open('./test.p',mode='rb') as test_data:
    test = pickle.load(test_data)

with open('./valid.p',mode='rb') as validation_data:
    validation = pickle.load(validation_data)


## extract the features and labels for training, test and validation from the loaded dataset.
# NOTE: above loaded dataset is in form of dict
X_train, Y_train = train['features'], train['labels']
print(X_train.shape)
print(Y_train.shape)

X_test, Y_test = test['features'],test['labels']
print(X_test.shape)
print(Y_test.shape)


X_validation, Y_validation = validation['features'],validation['labels']
print(X_validation.shape)
print(Y_validation.shape)

## shuffle the training dataset and convert all the images into grayscale and then normalize
X_train, Y_train = shuffle(X_train,Y_train)

# convert into grayscale
X_train_gray = np.sum(X_train/3,axis=3,keepdims=True)
X_test_gray = np.sum(X_test/3, axis = 3, keepdims=True)
X_validation_gray = np.sum(X_validation/3, axis=3, keepdims=True)

# normalize images
X_train_norm = (X_train_gray - 128)/128
X_test_norm = (X_test_gray - 128)/128
X_validation_norm = (X_validation_gray - 128)/128

print(X_train_norm.shape)

## create CNN architecture using Keras sequence
image_shape = X_train_norm[1].shape

cnn_model = Sequential()
cnn_model.add(Conv2D(32,(3,3), padding='same',strides=1, input_shape= image_shape,activation='relu'))
cnn_model.add(MaxPooling2D(pool_size=(2,2)))
cnn_model.add(Flatten())
cnn_model.add(Dense(units=32, activation='relu'))
cnn_model.add(Dense(units=43, activation='sigmoid'))

#compile the model
cnn_model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy'])

# train the model
cnn_model.fit(X_train_norm, Y_train,
              batch_size=500,
              nb_epoch=20,
              verbose=1,
              validation_data= (X_validation_norm,Y_validation))


# Result after traning: loss: 0.2459 - acc: 0.9519
#--------------------------------------------------

# check accuracy
score = cnn_model.evaluate(X_test_norm,Y_test, verbose=0)
print('Test accuracy = ',format(score[1]))

# Result: Test accuracy = 0.8051
plt.show()