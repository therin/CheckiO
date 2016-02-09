# -*- coding: utf-8 -*-
'''
The Hamming distance between two binary integers is the number of bit positions that differs (read more about the Hamming distance on Wikipedia). For example:
    117 = 0 1 1 1 0 1 0 1
     17 = 0 0 0 1 0 0 0 1
      H = 0+1+1+0+0+1+0+0 = 3
You are given two positive integers in decimal form. You should calculate the Hamming distance between these two numbers in binary form.
Input: A list of two integers.
Output: An integer.
Example:

checkio([117, 17]) == 3
checkio([1, 2]) == 2
checkio([16, 15]) == 5
How it is used: It's a basis for Hamming code and other linear error-correcting codes.
'''
def checkio(data):
    a, b = data
    a1 = "{0:08b}".format(a)
    b1 = "{0:08b}".format(b)
    a, b = data
    print 'first' + ' ' + a1
    print 'second' + ' ' + b1
    print sum(ch1 != ch2 for ch1, ch2 in zip(a1, b1))
    return sum(ch1 != ch2 for ch1, ch2 in zip(a1, b1))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([117, 17]) == 3, "First example"
    assert checkio([1, 2]) == 2, "Second example"
    assert checkio([16, 15]) == 5, "Third example"
