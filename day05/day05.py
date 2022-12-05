#!/usr/bin/env python3

import re
import sys

i= 1
# initiate data structure
stacks = []
n_stacks = 9  # make it simply, define the size here
for j in range(n_stacks):
    stacks.append([])

# helper fct
def print_stacks(st):
    for j in range(n_stacks):
        tmp = "%d: " % j
        for x in range(len(st[j])):
            tmp += st[j][x]
        print(tmp)


move_regex = re.compile("move (\d+) from (\d) to (\d)")

# here we go
with open("input") as f:
    for line in f.readlines():
        line = line.rstrip()
        if i < 9:
            # line 1-9 stack start configuration
            # print(line)
            for j in range(0, len(line), 4):
                crate = line[j:(j+3)]
                if crate != "   ":
                    #print("_%s_" % crate[1])
                    stacks[int(j/4)].insert(0, crate[1])
        # if i == 10:
            # print_stacks(stacks)

        # line 10 empty
        if i > 10:
            # print(line)

            # if i == 23:
                # print_stacks(stacks)

            # line 11ff start moving
            a = move_regex.findall(line)
            count, s_from, s_to = [int(x) for x in a[0]]
            s_from -= 1  # list position
            s_to -= 1
            # move sub_stack from s_from to s_to
            # question one
            #for j in range(count):
            #    stacks[s_to].append(stacks[s_from].pop())
            # question one
            tmp = []
            for j in range(count):
                tmp.append(stacks[s_from].pop())
            for j in range(count):
                stacks[s_to].append(tmp.pop())

            # if i == 23:
                # print(line)
                # print_stacks(stacks)
                # sys.exit()
        i += 1


print_stacks(stacks)

# top crades
tmp = ""
for j in range(n_stacks):
    tmp += stacks[j].pop()
print("results: %s" % tmp)

# wrong1 : LVZPSTTCZ