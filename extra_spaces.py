#Your code here
#You can import some modules or create additional functions
'''
Given string is a sentence, and words should be separated by only one space character. Remove all extra spaces.
Input data: A sentence in the string variable.
Output data: A sentence without extra spaces.
Example:
?
1
checkio('I  like   python') == "I like python"

'''
import re

def checkio(line):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.  
    news = line.split()
    news = " ".join(news)

    #ews = "".join(news)
    return news
    '''
    newlist = list(set(news))
    for some in news:
    	if some == "":
    		news.remove(some)
    		news.replace(" ","")
    c
    return newlist
'''
#Some hints
#you can use split and join methods from string.
#If you used replace() -- don't forget about three or four spaces
#Maybe regexp

#These "asserts" using only for self-checking and not necessary for auto-testing    
print checkio('I  like   python')

