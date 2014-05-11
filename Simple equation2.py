# -*- coding: utf-8 -*-
'''
The three robots reach the bottom of the pyramid and search for more clues. Sofia finds a small bit of text carved into the side of the wall.
“Hey, check this out.”
Nikola takes a look. “It’s hieroglyphics of some sort.”
“No, wait, it’s some kind of equation.” Says Sofia. “ a + b + c ≤ N. I wonder what it means.”
“Well, clearly we need to solve the equation.” Piped Stephen “Hangon, there’s another thing over here. It says ‘turn around and take __ steps to find the lost treasure
 of the Librarian.’ Wonder what that means...”
“THERE’S A SECRET TREASURE?! NOW WE HAVE TO FIGURE IT OUT!!” shouted Sofia at the top of her vocalizer
“If we can figure out all the answers, maybe it’ll give us the number of paces we need to take.”
“let’s do this.”
You are given four positive integers: A, B, C, N. If 0 ≤ a ≤ A , 0 ≤ b ≤ B and 0 ≤ c ≤ C, using these integers you should try to calculate the number of possible 
solutions to the following equation: a + b + c ≤ N.
Input: A list of four integers: A, B, C, N.
Output: An integer.
Example:

checkio([3, 2, 1, 4]) == 20
checkio([1, 1, 1, 1]) == 4
How it is used: Simple math software.
'''
import itertools
def checkio(data):	
	result = 0
	A, B, C, N = data
	list_a = []
	list_b = []
	list_c = []
	for i in range(A+1):
		list_a.append(i)
	for i in range(B+1):
		list_b.append(i)
	for i in range(C+1):
		list_c.append(i)
	print list_a,list_b,list_c
	some = list(itertools.product(list_a,list_b,list_c))
	print str(some)
	for entry in some:
		print entry
		if entry[0] + entry[1] + entry[2] <= N:
			result += 1
	return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([3, 2, 1, 4]) == 20, "First example"
    assert checkio([1, 1, 1, 1]) == 4, "Second example"
