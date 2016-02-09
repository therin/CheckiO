# -*- coding: utf-8 -*-
'''
The previous version of robots wasn't able to recognize big numbers. Thus we should make big numbers more readable and place a dot every three digits from the end 
in the numbers longer or equal than 4 digits.
There is no reason to insert dots in ordinal numbers like 1900th.
Input: A string containing numbers (unicode).
Output: Formatted string with dot-separated numbers (str).
Example:


checkio('123456') == '123.456'
checkio('333') == '333'
checkio('9999999') == '9.999.999'
checkio('123456 567890') == '123.456 567.890'
checkio('price is 5799') == 'price is 5.799'
checkio('he was born in 1966th') == 'he was born in 1966th'
How it is used: Auto-reporting software and document formatting.
'''

def checkio(txt):
    '''
   string with dot separated numbers, which inserted after every third digit from right to left
   '''
    words = txt.split()
    for word in words:
        if word.isdigit():
            new_word = '.'.join([word[::-1][i*3:(i+1)*3]
            for i in range(((len(word) - 1) // 3) + 1)])
            txt = txt.replace(word, new_word[::-1])
    return txt

'''
def checkio(text):    
    
    filtered_text = filter(str.isdigit, text)
    split_text = list(filtered_text)    
    split_text.reverse()
    print split_text
    length = len(split_text)
    print length
    for i in range(length):
        if i % 3 == 0 and i != 0:
            split_text.insert(i,'.')
    print ''.join(split_text)
    split_text.reverse()
    print ''.join(split_text)
    return ''.join(split_text)

'''

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('123456') == '123.456', "1st example"
    assert checkio('333') == '333', "2nd example"
    assert checkio('9999999') == '9.999.999', "3rd example"
    assert checkio('123456 567890') == '123.456 567.890', "4th example"
    assert checkio('price is 5799') == 'price is 5.799', "5th example"
    assert checkio('he was born in 1966th') == 'he was born in 1966th', "6th example"
