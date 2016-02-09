# -*- coding: utf-8 -*-
'''
Sophia's drones are too simple and can recognize symbols in only single words, digits or letters. She wants to teach the drones to understand basic
 commands which are represented as "words" consisted by letters and digits. For that, Sophia has uploaded "patterns," which describe the sequence of 
 digits and letters in the command. Unfortunately, the drones memory can only store integers and convert them into binary format for comparison. We 
 should help Sophia to write a module for the comparison of patterns and commands.
You are given a pattern as a positive integer and a command as a word. For the comparison, the drone should convert the integer pattern into binary 
form, append zeros to left for the command length and compare this combination with the command.
1 is a letter. 0 is a digit.
If the pattern and the command are coincided, then return True, else -- False. If pattern is longer than a command, then they are not coincided 
(For example - 8 = 1000 and "a").

For example. The pattern is 42 and the command is "12a0b3e4".
42 == 101010 in binary form, but this is not enough of length. Let's append zeroes -- "00101010". Then compare:
      42 == 00101010
12a0b3e4 == DDLDLDLD
--------------------
    True    VVVVVVVV
One more example -- 101 and "ab23b4zz":
     101 == 01100101
ab23b4zz == LLDDLDLL
--------------------
   False    XVXVXXXV
Input: Two arguments. A pattern as a positive integer and a command as a string.

Output: Is the pattern coincide with the command or not as a boolean.

Exampl
check_command(42, "12a0b3e4") == True
check_command(101, "ab23b4zz") == False
How it is used: In this mission you can learn how to store more complex data in simple numbers and how to work with simple patterns.
You can expand this concept and use more complex patterns (think about another number systems).

Precondition: 0 ≤ pattern < 231
0 < len(command) < 32
"command" contains only ASCII letters or digits.
'''

def check_command(pattern, command):
    result = []
    if len(command) < len(list(format(pattern, '0%ib'%len(command)))):
        return False
    print list(format(pattern, '0%ib'%len(command)))
    for i, item in enumerate(list(command)):
        #print list(format(pattern, '0%ib'%len(command)))[i]
        if list(format(pattern, '0%ib'%len(command)))[i] == str(1):
            #print list(format(pattern, '0%ib'%len(command)))[i], item
            if item.isdigit():
                return False
            else:
                result.append(True)
        if list(format(pattern, '0%ib'%len(command)))[i] == str(0):
            #print list(format(pattern, '0%ib'%len(command)))[i], item
            if not item.isdigit():
                return False
            else:
                result.append(True)
    print result
    return all(result)



if __name__ == '__main__':
    These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_command(42, u"12a0b3e4") == True, "42 is the answer"
    assert check_command(101, u"ab23b4zz") == False, "one hundred plus one"
    assert check_command(0, u"478103487120470129") == True, "Any number"
    assert check_command(127, u"Checkio") == True, "Uppercase"
    assert check_command(7, u"Hello") == False, "Only full match"
    assert check_command(8, u"a") == False, "Too short command"
    assert check_command(5, u"H2O") == True, "Water"
    assert check_command(42, u"C2H5OH") == False, "Yep, this is not the Answer"



