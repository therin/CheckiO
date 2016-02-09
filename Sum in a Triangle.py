# -*- coding: utf-8 -*-
'''
The musical notes shine as a melody begins to drift through the air. Harmonies intertwine and come to a crescendo. With the final note resonating through the air, a 
circular hole opens up in the center of the chamber floor. Sofia, Nikola and Stephen peer over the edge and see the top of an underground Pyramid.
“Well isn’t that something.” Breathed Nikola.
“It looks ancient. Maybe so prehistoric civilization constructed it?” Stephen pondered.
“Why would they make a Pyramid underground though?”
”That’s what we’re gonna find out!” Sofia exclaimed giddily and dropped through the hole and onto the cap of the Pyramid. Nikola and Stephen drop down after her as she 
begins to make her way down. “Oh, WOAH!” Sofia slips as a pile of rubble crumbles beneath her footing.
“Gotcha!” Stephen extends his arms out and snatches her out of thin air, saving her from a long fall.
“We’re going to have to be careful climbing down.” Nikola said once the dust settled. “Let’s try and take this one step at a time and try to find the sturdiest route 
down.”
“Okay, maybe you can lead the way then. I’d rather not fall all the way down.” Sofia shivered nervously recalling her slip.
Consider a list of lists in which the first list has one integer and each consecutive list has one more integer then the last. Such a list of lists would look like a
 triangle. You must write a program that will help Nikola and Stephen look for a route down the pyramid by stepping down and to the left or to the right. Your goal is
  to make sure this program will find the sturdiest route, that is, the route with the highest possible sum on its way down the pyramid.

Tip: Think of each step down to the left as moving to the same index location or to the right as one index location higher.

sum-in-triangles

Input: A list of lists. Each list contains integers.

Output: An Integer.

How it is used: This is a classical problem, which shows you how to use dynamic programming.
'''
import copy
def count_gold(pyramid):
    
    c = copy.deepcopy(pyramid)
    for l_index,level in enumerate(pyramid):
        for e_index,entry in enumerate(level):
            if l_index == 0 and e_index == 0:
                c[l_index][e_index] = pyramid[l_index][e_index]
            elif l_index == 1 and e_index == 0:
                c[l_index][e_index] = pyramid[l_index][e_index] + pyramid[0][0]
            elif l_index == 1 and e_index == 1:
                c[l_index][e_index] = pyramid[l_index][e_index] + pyramid[0][0]
            else:
                try:
                    #print "We are now on level" + ' ' + str(l_index)
                    if e_index-1 < 0:
                        c[l_index][e_index] = pyramid[l_index][e_index] + max(c[l_index-1][e_index],0)
                    else:
                        c[l_index][e_index] = pyramid[l_index][e_index] + max(c[l_index-1][e_index],c[l_index-1][e_index-1])
                    #print "First on the next level:" + ' ' + str(c[l_index-1][e_index-1])
                    #print "Second on the next level:" + ' ' + str(c[l_index-1][e_index])
                    #print "Adding:" + ' ' + str(pyramid[l_index][e_index]) + " at " + str((l_index,e_index)) + ' and ' + str(max(c[l_index-1][e_index-1],c[l_index-1][e_index])) + " = " + str(pyramid[l_index][e_index] + max(c[l_index-1][e_index-1],c[l_index-1][e_index]))
                except:
                    #print "Posiiton of a current entry:" + ' ' + str((l_index,e_index))
                    c[l_index][e_index] = pyramid[l_index][e_index] + max(0,c[l_index-1][e_index-1])
                    #print "Out of the list"

    return max(max(c))

'''
count_gold([
[7], 
[4,8],
[1,8,9],
[2,4,6,7],
[4,6,7,4,9],
[4,9,7,3,8,8]])

'''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"

