# -*- coding: utf-8 -*-
'''
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing 
ree respective marks in a horizontal, vertical, or diagonal row wins the game.
But we will not be playing this game. You will be the referee for this games results. You are given a result of a game and you must determine if the game ends in a win
 or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D."
x-o-referee
A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.
Input: A game's result. A list of strings (Unicode).
Output: "X", "O" or "D". A string.

Example:
checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X", "Xs wins"
checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"
How it is used: This task will help you to look at iterating data types. It is also used in games' algorithms.
'''
def checkio(game_result):
    result = 'D'
    rotated = zip(*game_result[::-1])
    for line in game_result:
        print line
        if "X" not in line and "." not in line:
            result = 'O'
            print "O wins in normal list"
        elif "O" not in line and "." not in line:
            result = 'X'
            print "X wins in normal list"
    for line in rotated:        
        print line
        if "X" not in line and "." not in line:
            result = 'O'
            print "O wins in normal list"
        elif "O" not in line and "." not in line:
            result = 'X'
            print "X wins in normal list"
    if game_result[0][0] == 'O' and  game_result[1][1] == 'O' and  game_result[2][2] == 'O':
        result = 'O'
    if game_result[0][0] == 'X' and  game_result[1][1] == 'X' and  game_result[2][2] == 'X':
        result = 'X'
    print result
    return result


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"

    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio(["OXO","XOX","OXO"]) == "O", "Os wins"