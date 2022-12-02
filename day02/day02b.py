#!/usr/bin/python 
# -*- coding: utf-8 -*-
#---------------------------------------
#
#
# Filename:    day02.py
# Description:
# Date:        02.12.22
#---------------------------------------

import sys


#         ro      pa     sc
values = {'A':1, 'B':2, 'C':3}

points = 0

with open('input') as f:
        for line in f.readlines():
            line = line.rstrip()
            opponent, result = line.split()
            opponent = values[opponent]
            # print("%s : %s" % (opponent, me))
            if result == 'X': # lose
                # points += 0
                # choose something worse than opponent
                choice = opponent - 1 
                if choice == 0:
                    choice = 3
            elif result == 'Y':  # draw
                points += 3
                # choose the same as opponent
                choice = opponent
            elif result == 'Z': #win
                points += 6
                # choose something better than opponent
                choice = opponent + 1 
                if choice == 4:
                    choice = 1
            else:
                print('no!')
                sys.exit(1)
            print("%s ::   %d vs. %d" % (result, choice, opponent))
            points += choice

print(points)




