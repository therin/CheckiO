# -*- coding: utf-8 -*-
'''
The Robots have discovered a new island and accidentally crashed on it. Tо survive, they need to create the largest rectangular field 
possible to make a landing strip. While surveying the land, they encountered a number of obstacles which they marked on their map. Each
square of the map is marked according to whether it contains grass (G), rock (R), water (W), shrubs (S), or trees (T). While the grass can 
be mowed and the shrubs can be dug from the ground, the water, rocks, and trees cannot be removed with the tools at their disposal. Given 
these obstacles, they need your help to determine the area of the largest possible rectangular field.

The island map is represented as a list of strings. Each list contains letter characters which indicate the conditions for each square of 
land (G, R, W, S, or T). The map is rectangular.

strip

Input: An island map as a list of strings.

Output: The maximum area of the largest possible rectangle that can be cleared as an integer.

Example:

checkio(['G']) == 1
checkio(['GS','GS']) == 4
checkio(['GT','GG']) == 2
checkio(['GGTGG','TGGGG','GSSGT','GGGGT','GWGGG','RGTRT','RTGWT','WTWGR']) == 9
How it is used: This concept touches on image and pattern recognition. If you solve the challenge with a Histogram search, you can use it
 for statistical analysis.

Precondition: 0 < |map| < 10
The map is rectangular.

Traverse the matrix once and store the following;

For x=1 to N and y=1 to N    
F[x][y] = 1 + F[x][y-1] if A[x][y] is 0 , else 0

Then for each row for x=N to 1 
We have F[x] -> array with heights of the histograms with base at x.
Use O(N) algorithm to find the largest area of rectangle in this histogram = H[x]

From all areas computed, report the largest.

'''

def checkio(landing_map):
    #print landing_map
    bad = 'RWT'
    stri = []
    binary = []
    for i in landing_map:
        for j in i:
            if j in bad:
                stri.append('1')
            else:
                stri.append('0')
        binary.append(stri)
        stri = []
    hist = binary[:]
    #print hist
    for i in range(len(binary)):
        print binary[i]
        for y in range(len(binary[i])):
            if binary[i][y] == str(0):
                if i == 0:
                    hist[i][y] = int(1)
                else:
                    hist[i][y] = int(1) + int(hist[i-1][y])
            else:
                hist[i][y] = int(0)
        print hist[i]
    maxrect = 0
    currect = 0
    for i in hist: 
        for j in range(len(i)): 
            maxcolumn = i[j] 
            rectbreadth = 0
            for k in range(j,len(i)):
                if i[j] > i[k]: 
                    maxcolumn = i[k]
                if i[k] > 0:
                    rectbreadth += 1 
                    currect = rectbreadth * maxcolumn 
                if currect > maxrect: 
                    maxrect = currect 
    return maxrect

'''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([u'G']) == 1, 'One cell - one variant'
    assert checkio([u'GS',
                    u'GS']) == 4, 'Four good cells'
    assert checkio([u'GT',
                    u'GG']) == 2, 'Four cells, but with a tree'
    assert checkio([u'GGTGG',
                    u'TGGGG',
                    u'GSSGT',
                    u'GGGGT',
                    u'GWGGG',
                    u'RGTRT',
                    u'RTGWT',
                    u'WTWGR']) == 9, 'Classic'

'''

print checkio(["GGSSGGSSG","GWSSGGTSG","GGSSGGSSG","GGSSGGSSG","GGSSWWSSG","GGSSGGSSG","GGSSGGSSG","GRRRRRRSG","GGSSGGSSG"])
