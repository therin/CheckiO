

def count_neighbours(grid, row, col):
    #print len(grid)
    counter = 0
    x = row
    y = col
    neigh = [(x2, y2) for x2 in range(x-1, x+2) for y2 in range(y-1, y+2) if -1 < x <= len(grid)-1 and -1 < y <= len(grid)-1 and (x != x2 or y != y2)]
    for item in neigh:
        #print item[0],item[1]
        if item[0] <= len(grid)-1 and item[1] <= len(grid)-1 and item[0] >= 0 and item[1] >= 0:
            if grid[item[0]][item[1]] == 1:
                print "Found some at " + str(item)
                counter +=1
    print counter
    return counter


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
