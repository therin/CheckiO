# -*- coding: utf-8 -*-
'''
Nicola has built a semi-automatized painting system, but this system can paint only one side of an item. After that, an operator must reload the 
machine and paint the other side (the system detects painted sides automatically). The painting process always takes the same amount of time. The 
camera can paint K surfaces at a time. Nicola wants Stephan to operate the painting machine and he needs to develop an algorithm for Stephan which 
will allow him to paint N (0 < N ≤ 10) surfaces in the shortest possible timeframe. Be careful that you don't paint the item more than two times.

system

The items are numbered from 0 to 9. You are given the paint holding capacity of the machine (K) and the quantity of items (N). You should return the
 sequence Stephen must paint as a string, where each action is the numbers of painted items. Actions separated by comma (",").

Input: Capacity of the painting system (K) and quantity of items (N) as integers.

Output: The sequence of actions as a string.


checkio(2, 3)  # "01,12,02"
checkio(6, 3)  # "012,012"
checkio(3, 6)  # "012,012,345,345"
checkio(1, 4)  # "0,0,1,1,2,2,3,3"
checkio(2, 5)  # "01,01,23,42,34"


Precondition:0 < K, N ≤ 10
'''

def checkio(capacity, number):
    items = [[str(N),2] for N in range(number)]
    #print items   
    operations = []
    while items:
        operation = ''
        print items[:capacity]
        for item in items[:capacity]:
            item[1] -= 1 
            operation += item[0]
        operations.append(operation)
        items = sorted ([I for I in items if I[1]>0] , key=lambda I:I[1], reverse=True)
        #print items
        #print operations
    #print operations
    return  ','. join(operations)



if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def check_solution(func, k, n, max_steps):
        result = func(k, n)
        actions = result.split(",")
        if len(actions) > max_steps:
            print("It can be shorter.")
            return False
        details = [0] * n
        for act in actions:
            if len(act) > k:
                print("The system can contain {0} detail(s).".format(k))
                return False
            if len(set(act)) < len(act):
                print("You can not place one detail twice in one load")
                return False
            for ch in act:
                details[int(ch)] += 1
        if any(d < 2 for d in details):
            print("I see no painted details.")
            return False
        if any(d > 2 for d in details):
            print("I see over painted details.")
            return False
        return True

    assert check_solution(checkio, 2, 3, 3), "1st Example"
#    assert check_solution(checkio, 6, 3, 2), "2nd Example"
#    assert check_solution(checkio, 3, 6, 4), "3rd Example"
#    assert check_solution(checkio, 1, 4, 8), "4th Example"
#    assert check_solution(checkio, 2, 5, 5), "5th Example"
