# -*- coding: utf-8 -*-
'''
There’s nothing here...” sighed Nikola.
“You’re kidding right? All treasure is buried treasure! It wouldn’t be treasure otherwise!” Said
Sofia. “Here, take these.” She produced three shovels from a backpack that seemed to appear out of thin air.
“Where did you get-”
“Don’t ask questions. Just dig!” She hopped on the shovel and began digging furiously.
CLUNK
“Hey we hit something.” Stephen exclaimed in surprise.
“It’s the treasure!” Sofia was jumping up and down in excitement.
The trio dug around the treasure chest and pulled it out of the hole and wiped the dirt off. Sofia tried grabbing the lid but it was locked. Nikola
studied the locking mechanism.
“I’ve seen this type of lock before. It’s pretty simple. We just need to check whether there is a sequence of 4 or more matching numbers and output a 
bool.”
“Easy enough. Let’s open this sucker up!” Sofia was shaking in excitement.
You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned 
horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

find-sequence
Input: A list of lists. Each list contains integers.

Output: A boolean. Whether or not a sequence exists.

Example:

checkio([
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
]) == True
checkio([
    [7, 1, 4, 1],
    [1, 2, 5, 2],
    [3, 4, 1, 3],
    [1, 1, 8, 1]
]) == False
checkio([
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1]
]) == True
checkio([
    [7, 1, 1, 8, 1, 1],
    [1, 1, 7, 3, 1, 5],
    [2, 3, 1, 2, 5, 1],
    [1, 1, 1, 5, 1, 4],
    [4, 6, 5, 1, 3, 1],
    [1, 1, 9, 1, 2, 1]
    ]) == True
How it is used: This concept is useful for games where you need to detect various lines of the same elements (match 3 games for example). 
This algorithm can be used for basic pattern recognition.

Precondition: 0≤N≤10
∀ x ∈ matrix : 0 < x < 10
'''
def checkio(matrix):

    def horizont(matrix):
        first = True
        counter = 0
        for i in range(len(matrix)):
            for y in range(len(matrix[i])):
                if y == 0:
                    pass
                #elif y == 1:
                    #if matrix[i][y] == matrix[i][y-1]:
                      #  counter +=2
                      #  print "found (2) "  + str(matrix[i][y]) + " at positions  " + str(i) + str(i-1) + " counter =  " + str(counter)
                      #  if counter >=4:
                      #      return True
                    #else:
                    #    counter = 0
                else:
                    if matrix[i][y] == matrix[i][y-1]:
                        if first:
                            counter +=2
                            print "found (2) "  + str(matrix[i][y]) + " at positions  " + str(i) + str(i-1) + " counter =  " + str(counter)
                            if counter >= 4:
                                return True
                            first = False
                        else:
                            counter +=1
                            print "found (1) "  + str(matrix[i][y]) + " at positions  " + str(i) + str(i-1) + " counter =  " + str(counter)
                            if counter >= 4:
                                return True
                    else:
                        counter = 0

            counter = 0
            first = True
        if counter >= 4:
            return True
        else:
            return False

    def vertical(matrix):
        first = True
        matrix1 = zip(*matrix[::-1])
        counter = 0
        for i in range(len(matrix1)):
            for y in range(len(matrix1[i])):
                if y == 0:
                    pass
                elif y == 1:
                    if matrix1[i][y] == matrix1[i][y-1]:
                        counter +=2
                        if counter >=4:
                            return True
                else:
                    if matrix1[i][y] == matrix1[i][y-1]:
                        counter +=1
                        if counter >= 4:
                            return True
                    else:
                        counter = 0
        if counter >= 4:
            return True
        else:
            return False

    def diagonals(matrix):
        counter = 0
        N = len(matrix)
        all_diagonals = [[matrix[y-x][x] for x in range(N) if 0<=y-x<N] for y in range(2*N-1)]

        for entry in all_diagonals:
            if len(entry) >= 4:
                #print entry
                for i in range(len(entry)):
                    if i == 0:
                        pass
                    elif i == 1:
                        if entry[i] == entry[i-1]:
                            counter +=2
                            #print "found "  + str(entry[i]) + '2'
                            if counter >=4:
                                return True
                    elif i == 2:
                        if entry[i] == entry[i-1]:
                            counter +=2
                            #print "found "  + str(entry[i]) + '2'
                            if counter >=4:
                                return True
                    else:
                        if entry[i] == entry[i-1]:
                            #print "found "  + str(entry[i]) + " at positions  " + str(i) + str(i-1)
                            counter +=1
                            #print str(counter)
                        if counter >= 4:
                            return True
            counter = 0
        return False

    def diagonals2(matrix):
        first = True
        counter = 0
        N = len(matrix)
        new_matrix = matrix[::-1]
        another_diagonals = [[new_matrix[y-x][x] for x in range(N) if 0<=y-x<N] for y in range(2*N-1)]
        for entry in another_diagonals:
            if len(entry) >= 4:
                #print entry
                for i in range(len(entry)):
                    if i == 0:
                        pass
                    elif i == 1:
                        if entry[i] == entry[i-1]:
                            counter +=2
                            #print "found (2) "  + str(entry[i]) + " at positions  " + str(i) + str(i-1)
                            if counter >=4:
                                #print 'Found 4'
                                return True
                        else:
                            counter = 0

                    elif i == 2:
                        if entry[i] == entry[i-1]:
                            counter +=1
                            #print "found ="  + str(entry[i]) + " at positions  " + str(i) + str(i-1)
                            if counter >=4:
                                #print 'Found 3'
                                return True
                        else:
                            counter = 0
                    else:
                        if entry[i] == entry[i-1]:
                            if first:
                                #print "found (2) "  + str(entry[i]) + " at positions  " + str(i) + str(i-1)
                                counter +=2
                                first = False
                                if counter >= 4:
                                    #print 'Found 2'
                                    return True
                            else:
                                #print "found +"  + str(entry[i]) + " at positions  " + str(i) + str(i-1)
                                counter +=1
                                if counter >= 4:
                                    #print 'Found 2'
                                    return True
                        else:
                            counter = 0
                            #print str(counter)
                            if counter >= 4:
                                #print 'Found 1'
                                return True
            counter = 0
            first = True
        return False
    print "found diagonal " + str(diagonals(matrix))
    print "found horizont " + str(horizont(matrix)) 
    print "found vertical " + str(vertical(matrix))
    print "found diagonals2 " + str(diagonals2(matrix))

    #return diagonals(matrix) or horizont(matrix) or vertical(matrix) or diagonals2(matrix)
    



'''
    def diagonals(matrix, k):
     rows = len(matrix)
     columns = len(matrix[0]) if matrix else 0
     #Main diagonals
     for r in range(rows - k + 1): # We don't have to check for the last rows
         for c in range(columns - k + 1):
             diag = [matrix[r+i][c+i] for i in range(k)]
             yield diag



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"

'''

checkio([[1,5,6,3,7,3,2],[2,9,1,1,5,3,8],[3,3,3,1,1,8,9],[4,2,1,3,2,1,4],[1,4,5,7,1,3,6],[4,5,8,6,1,1,2],[3,7,1,5,7,4,7]])