# -*- coding: utf-8 -*-
'''
Nikola picks up a strange circuit board. He flips it over and examines it closely. All of its elements are connected in a spiral and it is possible to connect the 
neighboring elements vertically and horizontally. He decides to play around with the circuit for fun and see what happens.
The map of the circuit consists of a series of square cells. The first element in the center is marked as 1, and continuing in a clockwise spiral, each other elements
 is marked in ascending order ad infinitum. On the map, you can move (connect cells) vertically and horizontally. For example, the distance between cells 1 and 9 is two
  moves and the distance between 24 and 9 is one move. You must help Nikola find the distance between any two elements on the map.
Input: A list of two marked cells (integers).
Output: The distance between the two elements. An Integer.
Example:

checkio([1, 9]) == 2
checkio([9, 1]) == 2
checkio([10, 25]) == 1
checkio([5, 9]) == 4
How it is used:
'''

def spiral(X, Y):
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            print (x, y)
            # DO STUFF...
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

print spiral(10,10)



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 9]) == 2, "First"
    assert checkio([9, 1]) == 2, "Reverse First"
    assert checkio([10, 25]) == 1, "Neighbours"
    assert checkio([5, 9]) == 4, "Diagonal"
    assert checkio([26, 31]) == 5, "One row"
    assert checkio([50, 16]) == 10, "One more test"