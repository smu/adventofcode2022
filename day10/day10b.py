#!/usr/bin/env python3


import re


# addx 2
# addx -6
# addx -11
# noop


re_noop = re.compile('noop')
re_add = re.compile('addx ((-)?\d*)')

cyc  = 0
reg = 1

def screen_print(cyc, spride_middle):
    # print("     %d - %d" % (cyc%40, reg))
    if abs((cyc%40) - spride_middle) <= 1:
        print('#', end='')
    else:
        print('.', end='')
    if (cyc+1) % 40 == 0:
        print()

with open('input') as f:
    for line in f.readlines():
        # print(line.strip())
        screen_print(cyc, reg)
        if re_noop.match(line):
            cyc += 1
        elif re_add.match(line):
            cyc += 1
            screen_print(cyc, reg)
            value = re_add.findall(line)[0][0]
            reg += int(value)
            cyc += 1
        # if cyc > 5:
            # break
