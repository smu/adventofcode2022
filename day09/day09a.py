#!/usr/bin/env python3


import sys
import numpy as np

size = 2000



class field:
    def __init__(self, size):
        self.field = np.full(shape = [size,size], fill_value='.')
        head_pos = [int(size/2),int(size/2)]  
        tail_pos = [int(size/2),int(size/2)]
        self.field[tail_pos[0],tail_pos[1]] = 'T'
        self.field[head_pos[0],head_pos[1]] = 'H'
        self.head_pos =head_pos
        self.tail_pos = tail_pos
        self.visited = np.full(shape = [size,size], fill_value='.')
        self.visited[tail_pos[0],tail_pos[1]] = '#'

    def print(self):
        print(self.field)
    
    def move(self, direction, steps, debug=False):
        # list are copied by references, so this should be sufficient
        head_pos = self.head_pos
        tail_pos = self.tail_pos
        field = self.field
        for s in range(1, steps+1):
            field[head_pos[0], head_pos[1]] = '.'
            print(s)
            # move head
            if direction == 'R':
                head_pos[1] += 1
            elif direction == 'L':
                head_pos[1] -= 1
            elif direction == 'U':
                head_pos[0] -= 1
            elif direction == 'D':
                head_pos[0] += 1
            else:
                print('ERROR')
                sys.exit(1)
            # move tail
            field[tail_pos[0], tail_pos[1]] = '#'
            if abs(head_pos[0] - tail_pos[0]) > 1 or \
               abs(head_pos[1] - tail_pos[1]) > 1:
                # connections is lost, we have to move the T
                delta_y = head_pos[0] - tail_pos[0] 
                #print('delta_y %d' % delta_y)
                if delta_y > 0:
                    tail_pos[0] += 1
                elif delta_y < 0:
                    tail_pos[0] -= 1
                delta_x = head_pos[1] - tail_pos[1]
                #print('delta_x %d' % delta_x)
                if delta_x > 0:
                    tail_pos[1] += 1
                elif delta_x < 0:
                    tail_pos[1] -= 1
            field[tail_pos[0], tail_pos[1]] = 'T'
            self.visited[tail_pos[0], tail_pos[1]] = '#'
            # update field
            field[head_pos[0], head_pos[1]] = 'H'
            if debug:
                self.print()

    def result_a(self):
        print(self.visited)
        return(np.count_nonzero(self.visited == '#'))


f = field(size)
f.print()

#with open("day09/input_example") as ff:
with open("day09/input") as ff:
    for line in ff.readlines():
        # print(line)
        direction, steps = line.split()
        steps = int(steps)
        print("%s %d" % (direction,steps))
        f.move(direction, steps, debug=False)

f.print()
print(f.result_a())

sys.exit(0)