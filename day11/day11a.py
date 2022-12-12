#!/usr/bin/env python3

import sys
import re
import math






class Monkey:
    def __init__(self):
        self.items = []
        self.other_monkeys = []
        self.config_lines = []
        self.test_true_monkey = None
        self.test_false_monkey = None
        self.operation_str = ''
        self.test_divide_by = 0
        self.item_inspections = 0

    def add_other_monkeys(self, monkeylist):
        self.other_monkeys = monkeylist


    def add_config_line(self, line):
        self.config_lines.append(line)

    def read_config(self):
        re_item =  re.compile('Starting items: ([\d, ]+)')
        re_operation = re.compile('Operation: (.*)')
        re_test = re.compile('Test: divisible by (\d+)')
        re_test_true = re.compile('If true: throw to monkey (\d)')
        re_test_false = re.compile('If false: throw to monkey (\d)')
        for l in self.config_lines:
            if re_item.match(l):
                items = re_item.findall(l)[0]
                self.items = [int(i) for i in items.split(',')]
            elif re_operation.match(l):
                op = re_operation.findall(l)[0]
                self.operation_str = op
            elif re_test.match(l):
                value = re_test.findall(l)[0]
                self.test_divide_by = int(value)
            elif re_test_true.match(l):
                monkey = int(re_test_true.findall(l)[0])
                self.test_true_monkey = monkey
            elif re_test_false.match(l):
                monkey = int(re_test_false.findall(l)[0])
                self.test_false_monkey = monkey
            # else:
                # print(l)

    def operation(self, item):
        re_plus = re.compile('new = old \+ (\d+)')
        re_times = re.compile('new = old \* (\d+)')
        re_times2 = re.compile('new = old \* old')
        if re_plus.match(self.operation_str):
            value = int(re_plus.findall(self.operation_str)[0])
            return(item + value)
        elif re_times.match(self.operation_str):
            value = int(re_times.findall(self.operation_str)[0])
            return(item * value)
        elif re_times2.match(self.operation_str):
            return(item * item)
        else:
            print(self.operation_str)
            sys.exit(1)

    def turn(self):
        # import pdb
        # pdb.set_trace()
        for i in range(len(self.items)):
            self.item_inspections += 1
            i = self.items.pop(0)
            print('Inspecting item %d' % i)
            # inspect
            i = self.operation(i)
            # / 3
            i = math.floor(i / 3)
            # test and  throw
            if i % self.test_divide_by  == 0:
                print('Throwing %i to %d' % (i, self.test_true_monkey))
                # print('%d' % id(self.other_monkeys[self.test_true_monkey]))
                self.other_monkeys[self.test_true_monkey].add_item(i)
            else:
                print('Throwing %i to %d' % (i, self.test_false_monkey))
                # print('%d' % id(self.other_monkeys[self.test_true_monkey]))
                self.other_monkeys[self.test_false_monkey].add_item(i)


    def add_item(self, item):
        self.items.append(item)
        # print('added item %d ' % item)

monkeys = []


with open('input') as f:
# with open('input_example') as f:
    m = None
    for line in f.readlines():
        line = line.strip()
        if re.match("^Monkey ", line):
            if m:
                m.read_config()
                monkeys.append(m)
            m = Monkey()
        m.add_config_line(line)
# add the last monkey
m.read_config()
monkeys.append(m)

# link all the monkeys to each other
i=0
for m in monkeys:
    print('%d: %d' % (i, id(m)))
    m.add_other_monkeys(monkeys)
    i+=1
print('-------------------')

for r in range(20):
    # start a round
    # i=0
    for m in monkeys:
        # print('%d: %d' % (i, id(m)))
        # print(m.items)
        m.turn()
        # print(m.items)
        # i+=1

for m in monkeys:
    print(m.items)


item_inspections = []
for m in monkeys:
    item_inspections.append(m.item_inspections)


item_inspections.sort()
print(item_inspections)
print(item_inspections[7] * item_inspections[6])
