#Your code here
#You can import some modules or create additional functions
'''
There is a list that contains integers, list of integers or nested lists. Put all integer values in one list.
Input data: A nested list or simple list.
Output data: One-dimensional list.

'''

def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    #replace this for solution
    
    answer = []
    for some in data:
    	if hasattr(some, "__iter__"):
    		answer.extend(checkio(some))
    	else:
    		answer.append(some)
    return answer



#These "asserts" using only for self-checking and not necessary for auto-testing
print checkio([1, 2, 3])# == [1, 2, 3], 'First example'
print checkio([1, [2, 2, 2], 4])# == [1, 2, 2, 2, 4], 'Second example'
print checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])# \
          # == [2, 4, 5, 6, 6, 6, 6, 6, 7], 'Third example'
