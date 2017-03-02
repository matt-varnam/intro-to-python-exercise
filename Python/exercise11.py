#!/usr/bin/python
#############
#Exercise 11#
#############

#Question1
import numpy as np
x = range(1,11)
a1 = np.array(x,dtype='int8')
a2 = np.array(x,dtype='float16')
print (a1.dtype)
print (a2.dtype)

#Question 2
zero1 = np.zeros([2,3,4])
print (zero1)
zero2 = np.ones([2,3,4])
print (zero2)
np.arange(1000)

#Question 3
a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
print (a[1])
print (a[1:4])

a = np.array([[2,  3.2, 5.5, -6.4, 2.2,  2.4], \
              [1, 22  , 4  ,  0.1, 5.3, -9  ], \
              [3,  1  , 2.1, 21  , 1.1, -2  ]]

print (a[:,3])
print (a[1:4,0:4])
print (a[1:, 2])
