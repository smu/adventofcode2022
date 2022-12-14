#!/usr/bin/env python3

import ast
import sys


DEBUG = False

def right_order(leftlist: list, rightlist: list, debug=True, level=0) -> bool or int:
    n = max(len(leftlist), len(rightlist))
    # n = len(leftlist)
    if debug:
        print('%s- Compare %s vs %s' % (" "*level, leftlist, rightlist))
        level += 1
        intend = ' '*level
    for i in range(n):
        if i == len(leftlist):
            if debug:
                print('%s- Right side ran out of items, so inputs are not in the right order' % intend)
            return(True)
        if i == len(rightlist):
            if debug:
                print('%s- Right side ran out of items, so inputs are not in the right order' % intend)
            return(False)
        left = leftlist[i]
        right = rightlist[i]
        if isinstance(left, int) and isinstance(right, int):
            if debug:
                print('%s- Compare %s vs %s' % (intend, left, right))
            if left < right:
                if debug:
                    print("%s- Left side is smaller, so inputs are in the right order" % intend)
                return(True)
            elif left > right:
                # not in the right order
                if debug:
                    print("%s- Right side is smaller, so inputs are not in the right order" % intend)
                return(False)
            else: #equal
                continue 
        else: # at least one element is a list
            if isinstance(right, int):
                if debug:
                    print("%s- Mixed types; convert right to [%d] and retry comparison" % (intend, right))
                right = [right,]
            elif isinstance(left, int):
                if debug:
                    print("%s- Mixed types; convert left to [%d] and retry comparison" % (intend, left))
                left = [left,]
            result = right_order(left, right, debug, level)
            if result is not None:
                return(result)


correct_pairs = []
i=1
# with open('day13/input_example') as f:
with open('day13/input') as f:
    while True:
        # print('pair: %d' % i)
        line = f.readline().strip()
        left = ast.literal_eval(line)
        line = f.readline().strip()
        right = ast.literal_eval(line)
        status = right_order(left, right, DEBUG)
        if status:
            # print('correct: %d' % i)
            correct_pairs.append(i)
        # empty line
        if DEBUG:
            print()
        line = f.readline()
        i += 1
        # if i > 3:
            # break
        if not line:
            break  # EOF
            

print(correct_pairs)
print(len(correct_pairs))
print(sum(correct_pairs))