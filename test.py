import cv2
from Hash_function import *

img = cv2.imread('test01.png')
a_point = (0,0)
b_point = (0,0)
size = 128

a_img = img[a_point[1]:a_point[1]+size,a_point[0]:a_point[0]+size]
b_img = img[b_point[1]:b_point[1]+size,b_point[0]:b_point[0]+size]
cv2.imshow('1',a_img)
cv2.imshow('2',b_img)
cv2.waitKey(0)
hash_value1 = average_hash(a_img)
print(hash_value1)
hash_value2 = average_hash(b_img)
print(hash_value2)
print(hamming_distance(hash_value1,hash_value2))