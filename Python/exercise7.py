#!/usr/bin/python
############
#Exercise 7#
############

#Question 1
a = [0,1,2]
b = a
print (a,b)
b[0] = 'hello'
print (a,b)
a.append(3)
print (a,b)

#Question 2
a = "can I change"
b = a
b = 'different'
print (a,b)

#Question 3
import copy
a = [0,1,2]
b = copy.deepcopy(a)
print (a,b)
b[0] = 'hello'
print (a,b)
