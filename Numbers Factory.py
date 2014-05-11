# -*- coding: utf-8 -*-
'''
You are given an integer N. For this mission, you should find the smallest positive number of X, such that the product of its digits is equal to N. If X does not exist, 
then return 0.
Let's examine the example. N = 20. We can factorize this number as 2*10, but 10 is not a digit. Also we can factorize it as 4*5 or 2*2*5. The smallest number for
 2*2*5 is 225, for 4*5 -- 45. So we select 45.
The one-digit numbers are answers themselves.
Hints: Remember prime numbers (numbers divisible by only one) and be careful with endless loops.
Input: A number N, an integer.
Output: The number X, an integer.
Example:
5
checkio(20) == 45
checkio(21) == 37
checkio(17) == 0
checkio(33) == 0
checkio(5) == 5
How it is used: This task will teach you how to work with numbers. You can factorize numbers and construct them again.
'''

def checkio(data):    
    if len(str(data) == 1:
       return data


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(5) == 5, "5th example"


checkio(20) == 45
#20 = 2 * 2 * 5 = 4 * 5
#45 < 54 < 225 < 252 < 522
checkio(17) == 0
#17 = 17
#17 is two digits number, so it's impossibl
checkio(5)
# 5 = 5
# 5 is one digit number, so itself
checkio(33) = 0
#33 = 3 * 11
#11 is two digits number, so we can not construct a number

checkio(21) == 37
# 21 = 7*3
# 37 < 73
checkio(x) == x #for 0<=x<=9