#!/usr/bin/python
#############
#Exercise 14#
#############

import numpy as np
import numpy.ma as MA

marr = MA.masked_array(range(10),fill_value=-999)
print (marr, marr.fill_value)
marr[2] = MA.masked
print (marr)
print (marr.mask)

narr = MA.masked_where(marr >= 7, marr)
print (narr)
print (narr.fill_value)
