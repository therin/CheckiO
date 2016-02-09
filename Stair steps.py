# -*- coding: utf-8 -*-
'''
There is a staircase with N steps and two platforms; one at the beginning, the other at the end of the stairs. On each step a number 
is written (ranging from -100 to 100 with the exception of 0.) Zeros are written on both platforms. You start going up the stairs from 
the first platform, to reach the top on the second one. You can move either to the next step or to the next step plus one. You must 
find the best path to maximize the sum of numbers on the stairs on your way up and return the final sum.
stair-steps
Input: Numbers on each stair as a list of integers.
Output: The final sum for the best way as an integer.
Example:
checkio([5, -3, -1, 2]) == 6
checkio([5, 6, -10, -7, 4]) == 8
checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393
checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125
How it is used: This is a classical example of the optimisation problem. It can show you the difference between the various methods of programming; 
such as dynamic programming and recursion.
Precondition:0 < |steps| ≤ 10
∀ x ∈ steps : -100 <; x < 100; x != 0
'''
def checkio(numbers):
    xs = numbers
    xs.append(0)
    ys = [0,xs[0]]
    #print ys
    #print xs[1:]
    for x in xs[1:]:
        #print ys, x,ys[-1],ys[-2]
        ys.append(x+max(ys[-1],ys[-2]))
    #print ys
    return ys[-1]


print checkio([5, 6, -10, -7, 4])



'''
   start = numbers[0]
    end = numbers[-1]
    path = []
    path = path + [start]
        print path
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([5, -3, -1, 2]) == 6, 'Fifth'
    assert checkio([5, 6, -10, -7, 4]) == 8, 'First'
    assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, 'Second'
    assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125, 'Third'
    print('All ok')

        graph = []
    for i in range(len(numbers)-1):
        if i < len(numbers)-2:
            graph.append([numbers[i],(numbers[i+1],numbers[i+2])])
    print graph
    start = numbers[0]

    xs = numbers
    xs.append(0)
    ys = [0,xs[0]]
    print ys
    print xs[1:]
    for x in xs[1:]:
        ys.append(x+max(ys[-1],ys[-2]))
    return ys[-1]

    

'''