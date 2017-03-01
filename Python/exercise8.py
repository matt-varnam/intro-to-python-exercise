#!/usr/bin/python
############
#Exercise 8#
############

def double_it(number):
    return number*2

print(double_it(2))
print(double_it(5.0))
print(double_it('hi'))

def calc_hypo(a,b):
    if type(a) not in [int,float]:
        print ('a is not an integer or float') 
        return False
    
    if type(b) not in [int,float]:
        print ('b is not an integer or float')
        return False

    if a <= 0:
        print('a cannot be negative')
        return False

    if b <= 0:
        print('b cannot be negative')
        return False

    hypo = (a**2 + b**2) **0.5
    return hypo

print(calc_hypo(3,4))
print(calc_hypo(1,'hi'))
print(calc_hypo(-1,4))
