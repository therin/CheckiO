'''
Calculate the quantity of 'a' letters in the given string.

Input:  A string.

Output: An integer. Quantity of letters "a" in a sentence.

Example:

?
1
2


'''
def checkio(data):

    counter = 0
    words = data.split()
    letters = []
    for word in words:
    	word1 = word.split()
    	letters.append(word1) 
    return data.count('a')

print checkio('This task is awesome!') #== 2
print checkio('All tasks are awesome and interesting') #== 4
