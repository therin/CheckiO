'''
You are given number of sticks (N). These sticks are represented in a list by their length (integers). For this
 mission, you should calculate the number of combinations that cannot form a complete triangle (including 
 	degenerated case, when a+b=c). If you can figure out which triangles do not work, you can help Nikola and
Stephen repair the generator.
For example: in the list of lengths [5, 2, 9, 6] the combinations (5, 2, 9) and (2, 9, 6) would not form a 
complete triangle. This means that out of all the possible combinations of numbers in that list, only 2 would 
not form a complete triangle.
Input: A list of integers.

Output: An integer.

Example:

?
1
2
3
'''
import itertools
def checkio(data):
    result = []
    counter = 0
    if len(data) == 3:
    	first = data[1] + data[2] >= data[0]
    	second = data[0] + data[2] >= data[1]
    	third = data[0] + data[1] >= data[2]
    	result.append(first)
    	result.append(second)
    	result.append(third)
    	if False in result:
    		counter += 1
        return counter
    else:
        combi = list(itertools.combinations(data,3))
        for comb in combi:
            result = []
    	    first = comb[1] + comb[2] >= comb[0]
    	    second = comb[0] + comb[2] >= comb[1]
    	    third = comb[0] + comb[1] >= comb[2]
    	    result.append(first)
    	    result.append(second)
    	    result.append(third)
    	    if False in result:
    		counter += 1
        return counter



print checkio([4, 2, 10]) #== 1
print checkio([1, 2, 3]) #== 0
print checkio([5, 2, 9, 6]) #== 2