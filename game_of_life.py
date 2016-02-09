# -*- coding: utf-8 -*-

def life_counter(state, tick_n):
  
    alive = {}
    for i in range(len(state)):
        for y in range(len(state[0])):
            if state[i][y] == 1:
                alive[i,y] = 1

    def nextgen(gen):
    # Function to get all neighbours for a specific cell
        def neighbour(item):
            x = item[0]
            y = item[1]
            # Calculate neighbours for each item
            #print [(x2, y2) for x2 in range(x-1, x+2) for y2 in range(y-1, y+2) if -1 < x <= 28 and -1 < y <= 28 and (x != x2 or y != y2)]
            return [(x2, y2) for x2 in range(x-1, x+2) for y2 in range(y-1, y+2) if -500 < x <= 509 and -500 < y <= 509 and (x != x2 or y != y2)]
        neighbours = map(neighbour,gen)
        neighbours_flat = [item for sublist in neighbours for item in sublist]
        neighbours_counted = {x:neighbours_flat.count(x) for x in neighbours_flat}
        survivors = list(set([key for key in neighbours_counted.keys() if (neighbours_counted[key] == 3 or neighbours_counted[key] == 2) and key in gen]))
        newborn = list(set([key for key in neighbours_counted.keys() if neighbours_counted[key] == 3]))
        return list(set(survivors + newborn))

    new_gen = [i for i in alive.keys()]

    for i in range(tick_n):
        new_gen = nextgen(new_gen)

    return len(new_gen)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 4) == 15, "Example"
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 15) == 14, "Little later"
    assert life_counter(((0, 1, 0),
                         (0, 0, 1),
                         (1, 1, 1)), 50) == 5, "Glider"
    assert life_counter(((1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1),
                         (0, 0, 0, 0, 0),
                         (1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1)), 100) == 16, "Stones"
    assert life_counter(((0,0,0,0,0,0,1,0),
                         (1,1,0,0,0,0,0,0),
                         (0,1,0,0,0,1,1,1),), 129) == 2
