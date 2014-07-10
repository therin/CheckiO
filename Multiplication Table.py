# -*- coding: utf-8 -*-
'''
After reading "Alice's Adventures in Wonderland," our robots decided to create their own "Multiplication table." Stephan would lead this
 mission (yeah, that probably was a bad idea). He forgot how to do multiplication and tried to invent a new method. It’s a rather strange 
 method if we may be so blunt.

In Stephan's version of multiplication, we convert numbers to binary representation without trailing zeroes. Then the first number is
 written vertically (up to down) and the second horizontally (left to right). With that, we fill a table with various binary operations
  for each crossing -- AND, OR, XOR, so we end up with three tables. In each table we convert rows to decimal and summarize it, then 
  summarize the results of three tables. Let's look at several examples.

You should help Stephan write a function to calculate this "multiplication". You are given two positive integers (n > 0), be careful with 
order of arguments.
Input: Two arguments as integers.
Output:
Example:
checkio(4, 6) == 38
checkio(2, 7) == 28
checkio(7, 2) == 18
    How it is used: In this task we play around with logical binary operations, the basis for computer science. Maybe you can find a use 
    for this subject in cryptography?
Precondition: 0 < x < 100
0 < y < 100
'''

def checkio(first, second):
    #firstbin = (format(first, '03b'))
    #secondbin = (format(second, '03b'))
    firstbin = list(bin(first))[2:]
    secondbin = list(bin(second))[2:]
    print firstbin,secondbin

    def sumthem(listi):
        counter = 0
        stri = ''
        result = []
        for i in listi:
            stri += str(i)
            counter +=1
            if counter == len(secondbin):
                #print stri
                result.append(int(stri,2))
                stri = ""
                counter = 0
        return sum(result)

    listAND =  [int(i) & int(y) for i in firstbin for y in secondbin]
    listOR =  [int(i) | int(y) for i in firstbin for y in secondbin]
    listXOR =  [int(i) ^ int(y) for i in firstbin for y in secondbin]
    #print listAND,listOR,listXOR
    #print sumthem(listAND),sumthem(listOR),sumthem(listXOR)
    return sumthem(listAND)+sumthem(listOR)+sumthem(listXOR)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18

'''
checkio(7, 2)
checkio(2, 7)
'''
