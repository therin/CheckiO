# -*- coding: utf-8 -*-
'''
When I start to feed my pigeon, a minute later two more fly by. And a minute later another 3. Then 4, and so on. One portion of food lasts a pigeon
 for a minute. In case there's not enough food for all the birds, the pigeons that came first, eat first. Pigeons are hungry animals and eat without 
 stopping. If I have N portions of wheat, how many pigeons will be fed with at least one portion of wheat?
pigeons
Input: A quantity of portions wheat, a positive integer.
Output: The number of fed pigeons, an integer.
Example:
checkio(1) == 1
checkio(2) == 1
checkio(5) == 3
checkio(10) == 6
How it is used: This is an example how we can make a model for various situations. Of course, the model has a limited approximation, but often we don't
 need a perfect model.
'''

def checkio(number):
    total_pigeons = 1
    newpigeons = 2
    mydict = {}
    feeded = 0
    while number > 0:
        for i in range(total_pigeons):
            if i in mydict and number > 0:
                print "Added one food for an existing pigeon"
                mydict[i] += 1
                number -=1
                print "Food left:" + ' ' + str(number)
            elif i not in mydict and number > 0:
                print "Added one food for a new pigeon"
                mydict[i] = 1
                number -=1
                print "Food left:" + ' ' + str(number)
            else:
                print "No more food left"
                break
        total_pigeons += newpigeons
        newpigeons +=1
        counter = 0
    for key, value in mydict.items():
        if value != 0:
            counter +=1
    print "Number of fed pigeons" + ' ' + str(counter)
    return counter


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio(1) == 1, "1st example"
    #assert checkio(2) == 1, "2nd example"
    #assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"


'''
    if (number<1):
        return 0
    else:
        total_pigeons = 1
        newpigeons = 2
        max_on_iter = []
        feeded = 0
        while ((feeded < total_pigeons) and (number > 0)):
            feeded += 1
            number -= 1
            total_pigeons += newpigeons
            newpigeons += 2
            print feeded
            max_on_iter.append(feeded)
            print max_on_iter
            return max(max_on_iter)
'''
