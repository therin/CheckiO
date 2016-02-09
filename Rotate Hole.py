# -*- coding: utf-8 -*-
'''
Sometimes humans build weird things. Our Robots have discovered and wish to use an ancient circular cannon loading system. This system looks like numbered pipes arranged in a circular manner. There is a rotating mechanism behind these pipes, and the cannons are attached to the end. This system is incredibly ancient and some of the cannons are broken. The loading automaton has a program with the pipe numbers which indicate where it should place cannonballs. These numbers cannot be changed as they are engraved into the pipes. We can, however, rotate the backend mechanism to change the correspondence between pipes and cannons. We should find each combination that we can rotate the backend mechanism so that all loaded cannonballs will be loaded into the still-working cannons. The loading automaton will load all of the balls simultaneously.

The pipes are numbered from 0 to N-1. The initial positions of the backend mechanism are represented as an array with 1 and/or 0. Each element describes a cannon behind the pipe; the 0th element describe 0th pipe. 1 is a working cannon and 0 is a broken cannon.

You know the pipe numbers where the automaton will load cannonballs (sometimes it loads several cannonballs into one cannon). Your goal is to find all the combinations that you can rotate the backend mechanism in a clockwise manner so that all of the cannonballs will be loaded into the working cannons. Rotation is described as an integer - how many units you should rotate clockwise. The result should be represented as a list of integers (variants) in the ascending order. The case when you don't need to rotate are described as 0 (but don't forget about other variants). If it's not possible to find a solution, then return [].

For example, the initial state is [1,0,0,0,1,1,0,1,0,0,0,1] and pipes numbers are [0,1]. If you rotate the mechanism by 1 or 8 units, then all balls which are be placed in the 0th and 1st pipes will be in cannons.

floor

Input: Two arguments.

A initial state as a list with 1 and/or 0
Pipe numbers for cannonballs as a list of integers
Output: The rotating variants as a list of integers or an empty list.

rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8]
rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == []
rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0]
rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5]
How it is used: This concept will acquaint you with circular data structures.

Precondition:
3 ≤ len(state) < 100
all(0 ≤ n < len(state) for n in pipe_numbers
'''
def rotate(state, pipe_numbers):
    return []


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"