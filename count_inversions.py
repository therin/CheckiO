def count_inversion(sequence):
    counter = 0
    for i,y in enumerate(sequence):
        if len(sequence) == 2:
            return 1
        if i+1 < len(sequence):
            if abs(y - (sequence[i+1])) > 1:
                counter += 1
                print y, sequence[i+1],abs(y - (sequence[i+1]))
    return counter



#if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
#    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
#    assert count_inversion((99, -99)) == 1, "Two numbers"
#    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
#    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")


print count_inversion((5, 3, 2, 1, 0))