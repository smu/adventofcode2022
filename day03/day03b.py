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
    i = 0
    threelines = []
    for line in f.readlines():
        line = line.rstrip()
        # get unique letters
        lineentries = list(set(list(line)))
        threelines.extend(lineentries)
        i += 1
        if i == 3:
            # auswerten
            threelines.sort()
            unique_letters = list(set(threelines))
            for letter in unique_letters:
                if threelines.count(letter) == 3:
                    print("found: %s in %s" % (letter, threelines))
                    priorities  += get_prio(letter)
            threelines = []
            i = 0

print(priorities)
