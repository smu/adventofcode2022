#!/usr/bin/python 
# -*- coding: utf-8 -*-
#---------------------------------------
#
#
# Filename:    day01.py
# Description:
# Date:        01.12.22
#---------------------------------------

#import sys


elfs = [0,]
elfcounter = 0

with open('input1') as f:
        for line in f.readlines():
            line = line.rstrip()
            if line:
                calories = int(line)
                elfs[elfcounter] += calories
            else:
                elfcounter += 1
                elfs.append(0)

# answer one
print(max(elfs))


# answer two

elfs.sort(reverse=True)
print(sum(elfs[0:3]))
