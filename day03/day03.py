#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#---------------------------------------
#
#
# Filename:    day03.py
# Description:
# Date:        02.12.22
#---------------------------------------


def get_prio(char):
    # Lowercase item types a through z have priorities 1 through 26.
    if ord(char) >= 97 and ord(char) <= 122:
        return(ord(char) - 96)
    # Uppercase item types A through Z have priorities 27 through 52.
    if ord(char) >= 64 and ord(char) <= 90:
        return(ord(char) - 64 + 26)


priorities = 0

with open('input') as f:
        for line in f.readlines():
            line = line.rstrip()
            n = len(line)
            half = int(n/2)
            one = line[0:(half)]
            two = line[(half):n]
            # print(len(one))
            # print(len(two))
            for i in range(len(one)):
                if one[i] in two:
                    print("Found: %s in %s %s" % (one[i], one, two))
                    priorities += get_prio(one[i])
                    # what about doublicate items? e.g. q in
                    #   zDqdpqMgMtgzthgDtQmz GPTVSTVrVGTFSVFFqNRF
                    #     ^  ^                               ^
                    # these should be ignored
                    break


print(priorities)
