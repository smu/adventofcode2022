#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#---------------------------------------
#
#
# Filename:    day04.py
#---------------------------------------

# In how many assignment pairs do the ranges overlap?

def get_range(string):
    return([int(i) for i in string.split('-')])

def a_overlaps_b(a,b):
    return(
            max(a) >= min(b) and min(a) <= max(b) 
            or
            max(b) >= min(a) and min(b) <= max(a) 
            )

count = 0

with open('input') as f:
        for line in f.readlines():
            line = line.rstrip()
            a, b = line.split(',')
            r_a = get_range(a)
            r_b = get_range(b)
            if a_overlaps_b(r_a, r_b):
                print("%s overlaps with %s" % (a,b))
                count += 1


print(count)

