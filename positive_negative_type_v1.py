#Convolutional Neural Networks

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


#Initialize CNN
classifer = Sequential()

#Convolution
classifer.add(Convolution2D(32,3,3, input_shape=(64,64,3), activation = 'relu'))

#Pooling
classifer.add(MaxPooling2D(pool_size=(2,2)))

#Flattening
classifer.add(Flatten())

#Full Connection
classifer.add(Dense(units=128, activation = 'relu'))
classifer.add(Dense(units=1,activation = 'sigmoid'))

#Compiling the CNN
classifer.compile(optimizer = 'adam',loss = 'binary_crossentropy', metrics = ['accuracy'])

#Part 2 - Fit CNN to image
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255,
                                      shear_range=0.2,
                                      zoom_range=0.2,
                                      horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size=(64,64),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size=(64,64),
                                            batch_size=32,
                                            class_mode='binary')

from IPython.display import display
from PIL import Image

classifer.fit_generator(training_set, steps_per_epoch=60,
                        epochs=5, validation_data=test_set,
                        validation_steps=20)
