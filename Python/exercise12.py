#!/usr/bin/python
#############
#Exercise 12#
#############

import numpy as np

#Question 1
arr = np.array([range(4),range(10,14)])
print (arr.size)
print (arr.shape)
print (arr.max(), arr.min())

#Question 2
print (arr.reshape(2,2,2))
print (arr.transpose())
print (arr.ravel())
print (arr.astype(np.float32))

#############
#Exercise 13#
#############

#Question 1
a = np.array([range(4),range(10,14)])
b = np.array([ 2,-1, 1, 0])
print (a*b)
b1 = b*100
b2 = b*100.0
print (b1,b2)
print (b1 == b2)
print (b1.dtype,b2.dtype)

#Question 2
arr = np.array([range(0,9)])
print (np.where(arr < 3))
print (np.less(arr,3))

condition = np.logical_or(arr < 3, arr > 8)
new_arr = np.where(condition, arr*5, arr*-5)

#Question 3
def wind(hor,vert, minmag = 0.1):
    mag = (hor**2 + vert**2)**0.5
    output = np.where(mag > minmag, mag, minmag)
    return output

u = np.array([[4,5,6],[2,3,4]])
v = np.array([[2,2,2],[1,1,1]])

print(wind(u,v))

u = np.array([[4,5,0.01],[2,3,4]])
v = np.array([[2,2,0.03],[1,1,1]])

print(wind(u,v))
