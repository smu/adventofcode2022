#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#---------------------------------------
#
#
# Filename:    day04.py
#---------------------------------------

# In how many assignment pairs does one range fully contain the other?

def get_range(string):
    return([int(i) for i in string.split('-')])

#def size(a):
#    return(a[1] - a[0])

def a_in_b(a,b):
    return(min(a) >= min(b) and max(a) <= max(b))

count = 0

with open('input') as f:
        for line in f.readlines():
            line = line.rstrip()
            a, b = line.split(',')
            r_a = get_range(a)
            r_b = get_range(b)
            if a_in_b(r_a, r_b) or a_in_b(r_b, r_a):
                print("%s in %s" % (a,b))
                count += 1


print(count)

