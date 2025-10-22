import cv2
import numpy as np

img1=np.zeros((300,300), dtype='uint8')

img2=np.zeros((300,300), dtype='uint8')

#creating shapes on images
circle=cv2.circle(img1,(150,150),100,(255),-1)
rectangle=cv2.rectangle(img2,(150,150),(250,250),(255),-1)

#applying thresholding
bitwise_and=cv2.bitwise_and(circle, rectangle)
bitwise_or=cv2.bitwise_or(circle, rectangle)
bitwise_xor=cv2.bitwise_xor(circle, rectangle)
bitwise_not_circle=cv2.bitwise_not(circle)

#showing images
cv2.imshow('orignal image 1',circle)
cv2.imshow('orignal image 2',rectangle)
cv2.imshow('Bitwise AND',bitwise_and)
cv2.imshow('Bitwise OR',bitwise_or)
cv2.imshow('Bitwise XOR',bitwise_xor)
cv2.imshow('Bitwise NOT on circle',bitwise_not_circle)
cv2.waitKey(0)
cv2.destroyAllWindows()