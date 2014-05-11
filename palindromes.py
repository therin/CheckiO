'''
An integer is said to be a palindrome if it is equal to its reverse in a string form. For example, 79197 
and 324423 are palindromes. In this task you will be given an integer N. You must find the smallest integer 
M >= N such that M is a prime number and M is a palindrome. 

Input: An integer.

Output: A prime palindrome. An integer.
'''

def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.

    #replace this for solution
    data = str(data)

    def ispal1(data):
    	data = str(data)
    	data1 = data[::-1]
    	return data == data1

    def isprime(data):
    	data = int(data)
    	return all(data % i for i in xrange(2, data))

    while not ispal1(data) or not isprime(data):
    	data = int(data) + 1
    	ispal1(data)
    return data


print checkio(31)
#==101
#checkio(130)==131
#checkio(131)==131
#'''
