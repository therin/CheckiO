#Your code here
#You can import some modules or create additional functions
'''
Given a list of integers. You should return a list consisting only of non-unique elements. So you need to remove all unique elements (contains in given list only once). Don't change order in a list. Example: [1, 2, 3, 1, 3]. 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
Input: A list of integers.
Output: A list of integers.
'''

def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.  
    news = []
    for dig in data:
    	if data.count(dig) > 1:
    	    news.append(dig) 
    return news

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#or remove elements from original list (but it's bad practice for many real cases)
#Loop over original list


#These "asserts" using only for self-checking and not necessary for auto-testing

assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"

