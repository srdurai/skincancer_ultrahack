import numpy as np
from keras.preprocessing import image

test_image = image.load_img('prediction_test_images/random_cancer_img_3.png',target_size=(64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifer.predict(test_image)
if result[0][0] > 0.5:
    print ("Possible Normal tissue")
else:
    print ("Possible Cancer tissue")