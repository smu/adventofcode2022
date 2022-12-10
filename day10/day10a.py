#!/usr/bin/env python3


import re


# addx 2
# addx -6
# addx -11
# noop


re_noop = re.compile('noop')
re_add = re.compile('addx ((-)?\d*)')

cyc  = 1
reg = 1

signal_strength = 0

with open('input') as f:
    for line in f.readlines():
        if re_noop.match(line):
            cyc += 1
            if cyc in [20, 60, 100, 140, 180, 220]:
                print('adding signal strength)')
                signal_strength += cyc * reg
        elif re_add.match(line):
            cyc += 1
            if cyc in [20, 60, 100, 140, 180, 220]:
                print('adding signal strength)')
                signal_strength += cyc * reg
            value = re_add.findall(line)[0][0]
            reg += int(value)
            cyc += 1
            if cyc in [20, 60, 100, 140, 180, 220]:
                print('adding signal strength)')
                signal_strength += cyc * reg
        else:
            print(line)

print(signal_strength)
