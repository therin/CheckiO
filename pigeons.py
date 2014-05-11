# -*- coding: utf-8 -*-
'''
When I start to feed my pigeon, a minute later two more fly by. And a minute later another 3. Then 4, and so on. One portion of food 
lasts a pigeon for a minute. In case there's not enough food for all the birds, the pigeons that came first, eat first. Pigeons are hungry 
animals and eat without stopping. If I have N portions of wheat, how many pigeons will be fed with at least one portion of wheat?

pigeons

Input: A quantity of portions wheat, a positive integer.

Output: The number of fed pigeons, an integer.

Example:
?
1
2
3
4
checkio(1) == 1
checkio(2) == 1
checkio(5) == 3
checkio(10) == 6
How it is used: This is an example how we can make a model for various situations. Of course, the model has a limited approximation,
 but often we don't need a perfect model.
 '''
def checkio(number):
	pigeon = 1
	fed_pigeon = 0
	while number > 0:
		number = number - pigeon
		print 'number' + ' ' + str(number)
		pigeon = pigeon =+ 1
		print 'pigeon' + ' ' + str(pigeon)
	print pigeon
	return pigeon

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
