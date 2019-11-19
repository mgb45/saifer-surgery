#!/usr/bin/env python
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') # in order to import cv2 under python3
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages') # append back in order to import rospy
from keras.applications.inception_v3 import InceptionV3
import numpy as np 
from keras.applications.inception_v3 import decode_predictions


if __name__ == "__main__":

    target_im = cv2.imread('cupcup.jpg')[100:399, 150:449]
    print(np.shape(target_im))
    cv2.imshow('new_im', target_im)
    target_im = np.expand_dims(target_im, axis=0)

    img_shape=(480,640,3)

    model = InceptionV3(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling='avg', classes=1000)

    res = np.array(model.predict(target_im)).flatten()
    print('Predicted:', decode_predictions(model.predict(target_im), top=3)[0])
