import numpy as np
from keras.preprocessing import image
test_image = image.load_img('testing/wt2.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'normal'
else:
    prediction = 'tumor found'
print (prediction)
