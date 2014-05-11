# -*- coding: utf-8 -*-
'''
A median is a numerical value separating the upper half of a list of numbers from the lower half. In a list where there are an 
odd number of entities, the median is the number found in the middle of the list. If the list contains an even number of entities,
n there is no single middle value, instead the median becomes the average of the two numbers found in the middle. For this mission,
 you are given a list of integers. With it, you must separate the upper half of the numbers from the lower half and find the median.

Input: A list of integers.

Output: A float.

Example:

?
1
2
3
4
checkio([1, 2, 3, 4, 5]) == 3
checkio([3, 1, 2, 5, 3]) == 3
checkio([1, 300, 2, 200, 1]) == 2
checkio([3, 6, 20, 99, 10, 15]) == 12.5
How it is used: The median has usage for Statistics and Probability theory. It has a very significant value for skewed 
distribution. For example, we want to know average wealth of people from a set of data -- 100 people earn $100 in month 
and 10 people earn $1,000,000. If we find the average, then we get $91,000. This is weird value and does nothing to show 
us the real picture. In this case the median would give to us more useful value and a better picture.
'''

def checkio(data):
	x = sorted(data)
	z = len(x)
	if z % 2 == 0:
		return (x[z/2]+x[(z/2)-1])/float(2)
	else:
		return x[z/2]

#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"