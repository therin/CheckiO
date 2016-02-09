
def boolean(x, y, operation):
    if operation == "conjunction":
        return x and y
    elif operation == "disjunction":
        return x or y
    elif operation == "implication":
        return (x and y) or not x
    elif operation == "exclusive":
        return x != y
    elif operation == "equivalence":
        return x == y
        
