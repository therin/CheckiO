'''
The robots found an open labyrinth. There are no walls, but only pits. If a player falls into a pit, he loses. 
The labyrinth is presented as a matrix (a list of lists): 1 is a pit and 0 is an empty cell. The labyrinth's size 
is 12 x 12 and the outer cells are also pits. Players start at cell (1,1). The exit is at cell (10,10). You need to
 find a route through the labyrinth. Players can move in only four directions--South (down [1,0]), North (up [-1,0]),
  East (right [0,1]), West (left [0, -1]). The route is described as a string consisting of different characters: "S"
  --South, "N"--North, "E"--East, and "W"--West.

checkio([
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1,1,1],
    [1,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,1,1,0,1,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1,1,1],
    [1,0,1,1,0,1,0,0,0,0,0,1],
    [1,0,1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,1,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]
]) == "SSSSSEENNNEEEEEEESSWWWWSSSEEEESS"
#be carefull with infinity loop
checkio([
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]
]) == "EEEEEEEEESSSSSSSSS"
checkio([
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
])
  '''

# -South (down [1,0]), North (up [-1,0]),  East (right [0,1]), West (left [0, -1]).


def checkio(labyrinth):
    move = labyrinth
    move[10][10] = 2
    global result
    result = []

    def search(x,y, done = ""):
        global result
        global movement
        if move[x][y] == 2:
            #print "Finished at " + str(x) + ',' + str(y)
            result.append(done)
            return True
        elif move[x][y] == 1:
            #print "Wall at "  + str(x) + ',' + str(y)
            return False
        elif move[x][y] == 3:
            #print "Was at "  + str(x) + ',' + str(y)
            return False

        #print "Visiting " + str(x) + ',' + str(y)
        result.append(done)
        #print "Add" + " " + done
        move[x][y] = 3
        if ((x < len(move)-1 and search(x+1, y, "S")) \
            or (x > 0 and search(x-1, y, "N")) \
            or (y > 0 and search(x, y-1, "W")) \
            or (y < len(move)-1 and search(x, y+1, "E"))):
            return True
        result.pop()
        return False

    search(1,1)
    result = "".join(result)
    return result


print checkio([
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,1],
[1,0,1,1,1,1,1,1,0,1,1,1],
[1,0,1,0,0,0,0,0,0,0,0,1],
[1,0,1,0,1,1,1,1,1,1,0,1],
[1,0,1,0,1,0,0,0,0,0,0,1],
[1,0,0,0,1,1,0,1,1,1,0,1],
[1,0,1,0,0,0,0,1,0,1,1,1],
[1,0,1,1,0,1,0,0,0,0,0,1],
[1,0,1,0,0,1,1,1,1,1,0,1],
[1,0,0,0,1,1,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
])