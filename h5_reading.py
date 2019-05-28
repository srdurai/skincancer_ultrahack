import h5py
import numpy as np
from tensorflow.keras.models import load_model
from keras.preprocessing import image

model = load_model('sample_model.h5')
test_image = image.load_img('prediction_test_images/random_cancer_img_3.png',target_size=(64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = model.predict(test_image)
if result[0][0] > 0.5:
    print ("Possible Normal tissue")
else:
    print ("Possible Cancer tissue")
