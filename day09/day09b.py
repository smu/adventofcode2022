#!/usr/bin/env python3


import sys
import numpy as np

size = 2000



class field:
    def __init__(self, size):
        self.field = np.full(shape = [size,size], fill_value='.')
        self.knots = []
        self.n_knots = 10  # knot 0 is the head
        for i in range(self.n_knots):
            self.knots.append([int(size/2),int(size/2)])
            #self.knots.append([size-5,5])
        self.field[self.knots[0][0], self.knots[0][1]] = 'H'
        self.visited = np.full(shape = [size,size], fill_value='.')
        # mark position of knot 9
        self.visited[self.knots[9][0],self.knots[9][0]] = '#'

    def print(self):
        print(self.field)

    def move_tails(self):
        # knot1 moves with head, the others move with the previous knots
        for i in range(1, self.n_knots):
            self.field[self.knots[i][0], self.knots[i][1]] = '.'
            if abs(self.knots[i-1][0] - self.knots[i][0]) > 1 or \
               abs(self.knots[i-1][1] - self.knots[i][1]) > 1:
                # connections is lost, we have to move the T
                delta_y = self.knots[i-1][0] - self.knots[i][0] 
                #print('delta_y %d' % delta_y)
                if delta_y > 0:
                    self.knots[i][0] += 1
                elif delta_y < 0:
                    self.knots[i][0] -= 1
                delta_x = self.knots[i-1][1] - self.knots[i][1]
                #print('delta_x %d' % delta_x)
                if delta_x > 0:
                    self.knots[i][1] += 1
                elif delta_x < 0:
                    self.knots[i][1] -= 1
            self.field[self.knots[i][0], self.knots[i][1]] = '%d' % i
    
    def move(self, direction, steps, debug=False):
        # move head
        for s in range(1, steps+1):
            self.field[self.knots[0][0], self.knots[0][1]] = '.'
            # move head
            if direction == 'R':
                self.knots[0][1] += 1
            elif direction == 'L':
                self.knots[0][1] -= 1
            elif direction == 'U':
                self.knots[0][0] -= 1
            elif direction == 'D':
                self.knots[0][0] += 1
            else:
                print('ERROR')
                sys.exit(1)
            # move tails
            self.move_tails()
            # mark position of knot 9
            self.visited[self.knots[9][0],self.knots[9][1]] = '#'
            # update field
            self.field[self.knots[0][0], self.knots[0][1]] = 'H'
            if debug:
                #self.print()
                print(self.visited)

    def result_a(self):
        # print(self.visited)
        return(np.count_nonzero(self.visited == '#'))


f = field(size)
f.print()

#with open("day09/input_example2") as ff:
with open("day09/input") as ff:
    for line in ff.readlines():
        # print(line)
        direction, steps = line.split()
        steps = int(steps)
        print("%s %d" % (direction,steps))
        f.move(direction, steps, debug=False)
        #f.print()

# f.print()
print('Result: %d ' % f.result_a())

sys.exit(0)