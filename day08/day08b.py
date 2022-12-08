#!/usr/bin/env python3


import numpy as np


def count_visible_trees(this_tree, other_trees):
    count = 0
    if len(other_trees) > 0:
        for i in range(len(other_trees)):
            count += 1
            # print('  -- %d %d' % (i, other_trees[i]))
            if this_tree <= other_trees[i]:
                break
    return(count)


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
    print(forest)
    scenic_score = np.zeros_like(forest)
    # check inner trees
    visible_trees = 0
    ncols, nrows = forest.shape
    for x in range(ncols):
        for y in range(nrows):
            this_tree = forest[x,y]
            # get score up
            trees_in_front = forest[0:x,y]
            visible_trees_up = count_visible_trees(this_tree, np.flip(trees_in_front))
            # get score right
            trees_in_front = forest[x,y+1:nrows]
            visible_trees_right = count_visible_trees(this_tree, trees_in_front)
            # print(visible_trees_right)
            # get score down
            trees_in_front = forest[x+1:ncols,y]
            visible_trees_down = count_visible_trees(this_tree, trees_in_front)
            # get score left
            trees_in_front = forest[x,0:y]
            visible_trees_left = count_visible_trees(this_tree, np.flip(trees_in_front))

            scenic_score[x,y] = visible_trees_up * visible_trees_right * visible_trees_down * visible_trees_left

    print(scenic_score)
    print('Result: %d ' % np.max(scenic_score))





