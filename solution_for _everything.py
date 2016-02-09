#We need a solution which can pass any case. The result of your solution should pass for any comparison with anything.
#
#You should write the function "checkio" which is called with one argument, the result will be compared with some other data (==, !=, etc) and the result of that comparison should be True.
#
#Input: Some data. Maybe that data over there.
#
#Output: The something as a something-else.
#
#Example:
#
#checkio({}) != [] # True
#checkio('Hello') < 'World' # True
#checkio(80) > 81 # True
#checkio(re) >= re # True
#checkio(re) <= math # True
#checkio(5) == ord # True

def checkio(x):
    class AlwaysTrue(object):
        def __ne__(self, x):
            return True
        def __eq__(self, x):
            return True
        def __lt__(self, x):
            return True
        def __le__(self, x):
            return True
        def __gt__(self, x):
            return True
        def __ge__(self, x):
            return True
    return AlwaysTrue()


'''

def checkio(anything):
    """
        try to return anything else :)
    """
    return True
    
if __name__ == '__main__':
    import re, math
    
    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'
    
    print('NO WAY :(')
'''