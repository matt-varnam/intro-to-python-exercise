#!/usr/bin/python
############
#Exercise 6#
############

#Question 1
s = 'I love to write python'
for char in s:
    print (char)
print (s[4])
print (s[-1])
print (len(s))
print s[0],# s[0,0], s[0,0,0] Can't break down any further?

#Question 2
s = 'I love to write python'
split_s = s.split()
for word in split_s:
    for chars in word:
	if chars == 'i':
	    print ("I found 'i' in: %s" % word)


for word in split_s:
    if word.find("i") > -1:
        print "I found 'i' in: '{0}'".format(word)

for word in split_s:
    if "i" in word:
        print "I found 'i' in: '{0}'".format(word) #in python2.7 {0} can be replaced with {}


#Question 3
something = "Completely Different"
dir(s)
print(something.count('t'))
print(something.find('plete'))
print(something.split('e'))
something = "Completely Different"
thing2 = something.replace("Different","Silly")
print(thing2)
# something[0] = 'B'
