# -*- coding: utf-8 -*-

'''
Crystal Row
A crystal or crystalline solid is a solid material whose constituents, such as atoms, molecules or ions, are arranged in a highly ordered microscopic structure, 
forming a crystal lattice that extends in all directions. The scientific definition of a "crystal" is based on the microscopic arrangement of atoms inside it, 
called the crystal structure. A crystal is a solid where the atoms form a periodic arrangement.

Because crystals are such an important resource, systems must be put in place to check the crystal quality during the growth and harvest periods. For our initial 
tests, we use random spot checks on the atomic lines composing each of the crystals. This crystal type contains two atoms composing the elements "X" (Xenatom) and "Z" (Zorium). In a well grown crystal, these atoms should alternate down the atomic line.

You are given a random line from crystal lattice as a sequence of letters "X" and "Z". The good line should have the periodic arrangement (one by one) as 
["X", "Z", "X", "Z"]. If any atoms are repeated, then this crystal is broken.

X - Z - X - Z - X - Z Good
Z - X - Z - X - Z - X Good
Z - X - X - Z - X - Z Bad
Z - X - Z - Z - Z - X Bad
Input: Atomic lines as a list of strings.

Output: The crystal quality as a boolean.

Example:

checkLine(["X", "Z", "X"]) == true
checkLine(["X", "Z", "X", "X"]) == false
Precondition:

1 < |line| ≤ 1000

∀ x ∈ line: x='X' OR x='Z'

How it is used:

This is first simple data structure and here you can learn how to work with a list. It's a simple concept which you can solve by just pausing to think
'''

def check_line(line):
    result = True
    for n,i in enumerate(line):
        if n == len(line)-1:
            return result
        if i == line[n+1]:
            result = False
    return result

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_line(["X", "Z", "X"]) == True
    assert check_line(["X", "Z", "X", "X"]) == False
    assert check_line(["X", "Z"]) == True
    assert check_line(["Z", "X"]) == True
    assert check_line(["Z", "X", "Z", "X", "Z", "Z", "X"]) == False
