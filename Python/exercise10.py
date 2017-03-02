#!/usr/bin/python
#############
#Exercise 10#
#############

x = range (6)
y = range (2,10,2)
a = set (x)
b = set (y)

print (a | b)
print (a & b)

band = ["mel", "geri", "victoria", "mel", "emma"]
counts = {}
for member in band:
    if member not in counts:
        counts[member] = 1
    else:
        counts[member] += 1

for member in counts:
    print (member,counts[member])

if {}: print ('hi')

d = {"maggie": "uk", "ronnie": "usa"}
dir(d.get)
print(d.get("wilhelm","Germany"))
print(d.get("ronnie"))
d.setdefault("mario","Italy")
