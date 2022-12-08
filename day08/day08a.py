#!/usr/bin/env python3


import numpy as np





values = []

# with open('input_example') as f:
with open('input') as f:
    for line in f.readlines():
        line = line.rstrip()
        oneline = []
        for i in range(len(line)):
            oneline.append(int(line[i]))
        values.append(oneline)
    forest = np.array(values)
    # print(forest)
    # check inner trees
    visible_trees = 0
    ncols, nrows = forest.shape
    for x in range(1, ncols-1):
        for y in range(1, nrows-1):
            this_tree = forest[x,y]
            # check visibility from top
            trees_in_front = forest[0:x,y]
            if (trees_in_front < this_tree).all():
                visible_trees += 1
                continue
            # check visibility from right
            trees_in_front = forest[x,y+1:nrows]
            if (trees_in_front < this_tree).all():
                visible_trees += 1
                continue
            # check visibility from bottom
            trees_in_front = forest[x+1:ncols,y]
            if (trees_in_front < this_tree).all():
                visible_trees += 1
                continue
            # check visibility from left
            trees_in_front = forest[x,0:y]
            if (trees_in_front < this_tree).all():
                visible_trees += 1
                continue

    print('Inner trees visible: %d' % visible_trees)

    # add outer trees
    visible_trees +=  2*ncols + 2*(nrows-2)

    print('Result: %d' % visible_trees)





