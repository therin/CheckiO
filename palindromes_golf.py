'''
An integer is said to be a palindrome if it is equal to its reverse in a string form. For example, 79197 
and 324423 are palindromes. In this task you will be given an integer N. You must find the smallest integer 
M >= N such that M is a prime number and M is a palindrome. 

Input: An integer.

Output: A prime palindrome. An integer.
'''

def golf(data):
  d=data+1
  while str(d)!=str(d)[::-1] or not all(d%i for i in range(2,d)):d+=1
  return d


'''


data = str(data+1)
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
'''

print golf(13)
#==101
#checkio(130)==131
#checkio(131)==131
#'''
