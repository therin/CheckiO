# -*- coding: utf-8 -*-


def digit_stack(commands):
    stack = []
    result = []
    for command in commands:
        if command == "POP":
            if stack:
                #print "deleting " + str(stack[-1])
                result.append(stack[-1])
                del stack[-1]
        elif command == "PEEK":
            if stack:
                result.append(stack[-1])
            else:
                pass
        else:
            stack.append(int(command.split(' ')[1]))
    return sum(result)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"

#print digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK","PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"])