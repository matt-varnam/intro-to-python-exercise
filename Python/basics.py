#!/usr/bin/python
course = 'python'
rating = 10
print (course)
print (rating)

b=3
c=4
a=(b**2+c**2)**0.5
print (a)

print (type(a))
print (type(b))
print (type(c))

int(a)
print (type(a))
print (str(a) + " squared equals " + str(b) + " squared plus " + str(c) + " squared.")

#Exercise 2

"""
Escape using Ctrl + C
while True:
    print ('hi')
"""
while 1 == 2:
    print('hi')

mylist =[23,"hi",2.4e-10]
count = 0
while count < 3:
    item = mylist[count]
    print (item, mylist.index(item))
    count += 1

x = 1
if x: print x, " is True" #Output "1 is True"
x = 22.1
if x: print x, " is True" #Output "22.1 is True"
x = "hello"
if x: print x, " is True" #Output "hello is True"
x = [1,2]
if x: print x, " is True" #Output "[1,2] is True"
x = 0
if x: print x, " is True" #Output ""
x = 0.0
if x: print x, " is True" #Output ""
x = None
if x: print x, " is True" #Output ""
x = False
if x: print x, " is True" #Output ""
x = ""
if x: print x, " is True" #Output ""
x = []
if x: print x, " is True" #Output ""
x = {}
if x: print x, " is True" #Output ""
x = ()
if x: print x, " is True" #Output ""

##Exercise 3
mylist = [0,1,2,3,4,5]
print(mylist[1])
print(mylist[len(mylist-2)]
print(mylist[:])
print(mylist[1:4]

one_to_ten = range(1,11)
one_to_ten[0] = 10
one_to_ten.append(11)
twelve_to_fourteen = [12,13,14]
one_to_ten.extend(twelve_to_fourteen) #Same as one_to_ten + twelve_to_fourteen

forward = []
backward = []
values = ["a", "b", "c"]
for value in values:
    forward.append(value)
    backward.insert(0,value)
print (forward)
print (backward)
forward.reverse()
if forward == backward:
    print('Check completedd')
