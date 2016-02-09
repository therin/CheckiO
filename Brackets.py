'''
Given an expression with numbers, brackets and operators. But in this task only brackets are important. Brackets 
can be one of three types -- "{}" "()" "[]". Brackets are determine the scope or restricted some expression. 
So each if was opened, then must be closed with the same type. The scopes of brackets must not intersected. 
You should to make a decision correct an expression or not. Don't care about operators and operands.
Input: An expression with different of types brackets.
Output: A boolean. Correct an expression or not.
Example:
?
1
2
3
4
5
checkio("((5+3)*2+1)") == True
checkio("{[(3+1)+2]+}") == True
checkio("(3+{1-1)}") == False
checkio("[1+1]+(2*2)-{3/3}") == True
checkio("(({[(((1)-2)+3)-3]/3}-3)") == False

'''
def checkio(data):
    brackets = {'}':'{', ')':'(', ']':'['}
    stack = []
    for c in data:
        if c in brackets.values(): stack.append(c)
        elif c not in brackets: pass
        elif c in brackets and stack and brackets[c] == stack[-1]:
            stack.pop()
        else: return False
    return not stack

print checkio("((5+3)*2+1)")
checkio("{[(3+1)+2]+}")
checkio("(3+{1-1)}")
checkio("[1+1]+(2*2)-{3/3}")
checkio("(({[(((1)-2)+3)-3]/3}-3)")