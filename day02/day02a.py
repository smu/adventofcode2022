#!/usr/bin/python 
# -*- coding: utf-8 -*-
#---------------------------------------
#
#
# Filename:    day02.py
# Description:
# Date:        02.12.22
#---------------------------------------

#import sys
#         ro      pa     sc     ro,    pa     sc
values = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}

points = 0

with open('input') as f:
        for line in f.readlines():
            line = line.rstrip()
            opponent, me = line.split()
            me = values[me]
            opponent = values[opponent]
            # print("%s : %s" % (opponent, me))
            points += me
            # draw
            if me == opponent:
                points += 3
            elif me == 3 and opponent == 1:
                # S vs R, i lost
                pass
            elif me == 1 and opponent == 3:
                # R vs S, i won
                points += 6
            else:
                # all the other cases
                if me > opponent:
                    # i won
                    points += 6

print(points)




