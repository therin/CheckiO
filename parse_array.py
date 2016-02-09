# -*- coding: utf-8 -*-
'''
In this task you you already have the solution. The problem is that it has a bug and you must try to find and fix it. 
"import", "exec" and "eval" don't work for this task.
You are given a string that contains a list with integers or nested lists. The integers could have single plus or minus sign before them.
 If the input string does not contain an array, then raise ValueError. For an incorrectly formatted string -- raise ValueError. Elements
  of the array are separated by commas.
Input: A string.
Output: The list with nested lists or integers.
Precondition: depth < 5
∀ x ∈ data : -1000 < x < 1000
'''
WHITESPACE_STR = ' \t\n\r'


def parse_array(s, _w=WHITESPACE_STR, _sep=","):
    array = None
    stack1 = []
    accumulator = ""
    closed_flag = False
    sep_flag = False
    whitespace_flag = False
    started_flag = False
    for ch in s:
        if ch in _w:
            whitespace_flag = True
            continue
        if ch == "[":
            if started_flag and not stack1:
                raise ValueError("Wrong string.")
            if closed_flag or accumulator:
                raise ValueError
            in_array = []
            if stack1:
                stack1[-1](in_array)
            else:
                array = in_array

                started_flag = True
                print "open bracket"
            stack1.append(in_array.append)
        elif not started_flag:
            raise ValueError("Wrong string.")
        elif ch == "]":
            if not stack1:
                raise ValueError("Wrong string.")
            if accumulator:
                stack1[-1](int(accumulator))
                accumulator = ""
            stack1.pop()
            started_flag = False
            closed_flag = True
            print "close bracket"
            sep_flag = False
            whitespace_flag = False
        elif ch in _sep:
            if accumulator:
                stack1[-1](int(accumulator))
                print "Put data in array"
                accumulator = ""
            elif closed_flag:
                pass
            else:
                raise ValueError("Wrong string.")
            sep_flag = True
            closed_flag = False
            print "open bracket"
            whitespace_flag = False
        else:
            if whitespace_flag and accumulator or closed_flag:
                raise ValueError
            accumulator += ch
            print "Adding char"
        whitespace_flag = False
    if not array is None and not stack1:
        return array
    else:
        raise ValueError("Wrong string")

print parse_array("[[2]")
#print parse_array("[[2]")
#print parse_array("[[[2,3,[1]], 2, 3]")