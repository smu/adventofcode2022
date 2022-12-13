#!/usr/bin/env python3

import numpy as np
import sys


class Point:
    def __init__(self, y, x, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.childs = []

    def add_child(self, point):
        self.childs.append(point)
    
    def __str__(self) -> str:
        return("%d,%d,(%d)" % (self.y, self.x, self.z))

Start_Point = None
End_Point = None
matrix = []
#with open('example_input') as f:
with open('input') as f:
    y=0
    for line in f.readlines():
        line = line.strip()
        row = []
        x=0
        for i in range(len(line)):
            char = line[i]
            if char == 'S':
                char = 'a'
                Start_Point = Point(y,x,0)
            elif char == 'E':
                char = 'z'
                End_Point = Point(y,x,25)
            pixel = ord(char) - ord('a')
            row.append(pixel)
            x += 1
        matrix.append(row)
        y += 1

field = np.array(matrix)
# print(field)

# print(field[0,5])
# sys.exit()


def check_point(field, visited, y, x, ref_z):
    '''returns true, if point(x,y) can be used'''
    # print("%d %d" % (y, x))
    ydim, xdim = field.shape
    if x < 0 or x >= xdim or y < 0 or y >= ydim:
        return(False)
    if visited[y, x] > 0:
        # allready visited or startpoint
        return(False)
    # print("  %d,%d      field size: %d x %d" % (y,x, ydim, xdim))
    # print("  Visit status: %d" % visited[y, x])
    # print('  Hoehen: Ref: %d  Punkt %d' % (ref_z, field[y,x]))
    if field[y,x] - ref_z <= 1:
        return(True)
    else:
        return(False)


def check_neighboring_points(field, visited, point):
    # print("Checking Point %s" % point)
    possible_ways = []
    # upper pixel
    if check_point(field, visited, point.y-1, point.x, point.z):
        possible_ways.append([point.y-1, point.x])
    # down
    if check_point(field, visited, point.y+1, point.x, point.z):
        possible_ways.append([point.y+1, point.x])
    # left
    if check_point(field, visited, point.y, point.x-1, point.z):
        possible_ways.append([point.y, point.x-1])
    # right
    if check_point(field, visited, point.y, point.x+1, point.z):
        possible_ways.append([point.y, point.x+1])
    return(possible_ways)


def weglaenge(Start_Point):
    # a second array, to keep track of the points that we got visited
    visited = np.zeros_like(field)
    visited[Start_Point.y, Start_Point.x] = '1'
    visited[End_Point.y, End_Point.x] = '-1'
    # breitensuche...
    points = [Start_Point, ]
    endfound = False
    iteration = 1
    while not endfound:
        nextpoints = []
        # print("Iteration %d" % iteration)
        for p in points:
            for pp in check_neighboring_points(field, visited, p):
                if visited[pp[0], pp[1]] == -1:
                    print('YES')
                    endfound = True
                    return(visited.max())
                    #break
                visited[pp[0], pp[1]] = iteration
                childP = Point(pp[0], pp[1], field[pp[0],pp[1]])
                p.add_child(childP)
                nextpoints.append(childP)
        # if endfound:
            # break
        if nextpoints:
            #print('Next iteration: %s' % ["%s" % p for p in nextpoints])
            points = nextpoints
            iteration += 1
        else:
            if not endfound:
                print('No way??')
                return(False)
                break
    # print(visited)


print(weglaenge(Start_Point))


minimalway = 999999

ydim, xdim = field.shape
for y in range(ydim):
    for x in range(xdim):
        elevation = field[y,x]
        if elevation == 0:
            p = Point(y, x, elevation)
            #print(p)
            bla = weglaenge(p)
            print(bla)
            if bla and bla < minimalway:
                minimalway = bla

print(minimalway)