# -*- coding: utf-8 -*-
'''
In mathematics, a repeating decimal is a way of representing a rational number. A decimal representation of a number is called a repeating decimal if at some point 
there is some finite sequence of digits that is repeated infinitely. For example: the decimal representation of 1/3 = 0.3333333… or 0.(3) becomes periodic just after 
the decimal point, repeating the single-digit sequence "3" infinitely. Here is another example is 27/26 = 1.0384615384615385… or 1.0(384615), where the decimal becomes
 periodic after the second digit past the decimal point, repeating the sequence "384615" infinitely. Rational numbers are numbers which can be expressed in the form a/b 
 where a and b are integers and b is not zero. This form is known as a common fraction. Read more about this at Wikipedia.

You will need to convert a fraction into decimal representation. If the decimal is repeating, you should represent it using the brackets format seen above. You have a
 list of two integers, the first is the fractions numerator and the second is its denominator. For this task, you will need to return the fraction in decimal 
 representation as a string.
 repeatin-decimal
Input: A list of two integers as a numerator and denominator.

Output: A decimal representation of the fraction in bracket format as a string.

Example:

checkio([1, 3]) == "0.(3)", "First"
checkio([5, 3]) == "1.(6)", "Second"
checkio([3, 8]) == "0.375", "Third"
checkio([7, 11]) == "0.(63)", "Fourth"
checkio([29, 12]) == "2.41(6)", "Fifth"
checkio([11, 7]) == "1.(571428)", "Sixth"
How it is used: Mathematical software.
'''


#from __future__ import division

def convert(numerator, denominator):

    # If repetition detection is off, you must 
    # specify a limit on the digits returned 
    #numerator, denominator = fraction
    digit_limit = None
    decimal_found = False
    detect_repetition = True
    v = numerator // denominator
    numerator = 10 * (numerator - v * denominator)
    answer = str(v)
    answer += '.'
    
    # Maintain a list of all the intermediate numerators 
    # and the length of the output at the point where that 
    # numerator was encountered. If you encounter the same 
    # numerator again, then the decimal repeats itself from 
    # the last index that numerator was encountered at. 
    states = {}
    
    while numerator > 0 and (digit_limit == None or digit_limit > 0):
        
        if detect_repetition:
            prev_state = states.get(numerator, None)
            if prev_state != None:
                start_repeat_index = prev_state
                non_repeating = answer[:start_repeat_index]
                repeating = answer[start_repeat_index:]
                return non_repeating + '(' + repeating + ')'
            states[numerator] = len(answer)
            print states

        
        v = numerator // denominator
        answer += str(v)
        numerator -= v * denominator
        numerator *= 10
        if digit_limit != None:
            digit_limit -= 1

    
    if numerator > 0:
        return answer + '...'
    return answer

#print checkio([3, 8])
print convert(1, 3)

'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 3]) == "0.(3)", "1/3 Classic"
    assert checkio([5, 3]) == "1.(6)", "5/3 The same, but bigger"
    assert checkio([3, 8]) == "0.375", "3/8 without repeating part"
    assert checkio([7, 11]) == "0.(63)", "7/11 prime/prime"
    assert checkio([29, 12]) == "2.41(6)", "29/12 not and repeating part"
    assert checkio([11, 7]) == "1.(571428)", "11/7 six digits"
'''