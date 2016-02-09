# -*- coding: utf-8 -*-
'''
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter
 returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation
bols and whitespaces, only letters. If you have two or more letters with the same frequency, then return the letter which comes first in the alphabet. 
(Ex: we have "b" and "f" as the most frequent, then return "b")

Input: A text for analysis. A string (Unicode).

Output: The most frequent letter in lower case. A string.

checkio("Hello World!") == "l"
checkio("How do you do?") == "o"
checkio("One") == "e"
checkio("Oops!") == "o"
checkio("AAaooo!!!!") == "a"
How it is used: For most decryption tasks you need to know the frequency of occurrence for various letters in a text. For example, we can easily 
crack a simple addition or substitution cipher if we know the frequency in which letters appear. This is interesting stuff for language experts!
'''
import re
from operator import itemgetter
def checkio(text):
    text_lower = text.lower()
    mydict = {}
    text_filtered = re.sub('[^abcdefghijklmnopqrstuvwxyz]', '', text_lower)
    text_split = list(text_filtered)
    #print text_split
    for i in text_split:
            if i in mydict:
                #print "Added one existing letter"
                mydict[i] += 1
            elif i not in mydict:
                #print "Added one more letter"
                mydict[i] = 1
    #print sorted([(key) for (key,value) in mydict.items()])
    if all(val==mydict.values()[0] for val in mydict.values()):
        one = sorted([(key) for (key,value) in mydict.items()])
        return one[0]
    return max(mydict,key=mydict.get)
'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
'''

print checkio(u"fsbd")
