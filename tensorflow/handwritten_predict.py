import numpy as np 
# To save and load model
from keras.models import load_model 
from keras.datasets import mnist
import matplotlib.pyplot as plt


model = load_model('csi_training_handwritten.h5')

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# get a slice 
test_images = test_images[1:5]

# reshape the test images
test_images = test_images.reshape(test_images.shape[0], 28, 28)
print("test images shape - {}".format(test_images.shape))

# loop over each of the test images
for i, test_image in enumerate(test_images, start=1):
	org_image = test_image
	# reshape the test image to [1x784] format so that our model understands
	test_image = test_image.reshape(1,784)
	prediction = model.predict_classes(test_image, verbose=0)
	print("The digit is - {}".format(prediction[0]))
	plt.subplot(220+i)
	plt.imshow(org_image, cmap=plt.get_cmap('gray'))
plt.show()
