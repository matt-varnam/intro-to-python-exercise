#!/usr/bin/python
############
#Exercise 5#
############

#Question 1
with open('weather.csv', 'r') as myfile:
    data = myfile.read()
print data

#Question 2
print("They think it's all over!")
with open('weather.csv', 'r') as myfile:
    liner = myfile.readline()[:-1]
    while liner:
	    if liner != "":
            print (liner)
	    liner = myfile.readline()[:-1]

print("It is now!")

#Question 3
with open('weather.csv','r') as myfile:
    liner = myfile.readline()
    rain = []
    for line in myfile.readlines():
        print (line[:-1])
	r = line.strip().split(",")[-1]
        r = float(r)
        rain.append(r) 
print (rain)
with open('rainfall.csv','w') as myfile:
    for fall in rain:
	myfile.write(str(fall)+"\n")

#Question 4
import struct
bin_data = struct.pack("bbbb", 123,12,45,34)
with open('mybinary.dat','wb') as myfile:
    myfile.write(bin_data)

with open('mybinary.dat','r') as myfile:
    bin_data2=myfile.read()
    data = struct.unpack("bbbb",bin_data2)
    print (data)


