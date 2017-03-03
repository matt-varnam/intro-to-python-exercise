#!/usr/bin/python
#############
#Exercise 15#
#############
import numpy as np
from csv import reader

time = np.array([])
temp = np.array([])

def convert_time(tm):
    tm = datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f")
    return tm

def convert_temp(temp):
    value = temp.string('+').strip('C').lstrip("0")
    return float(value) + 273.15

with open('sample-serial-temperature-2h.tsv', 'r') as myfile:
    tsvreader = reader(tsvfile, delimiter='\t')
    liner = myfile.readline()[:-1]
    while liner:        
        if liner != "":        
            split_line = liner.split("/t")
            print split_line
            tim = split_line[0]
            tem = split_line[1]
            np.append(time,tim)
            np.append(temp,tem)
        liner = myfile.readline()[:-1]

print time
print temp
