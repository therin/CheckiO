def transpose(data):
    print map(list, zip(*data))
    return map(list, zip(*data))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert transpose([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]) == [[1, 4, 7],
                                      [2, 5, 8],
                                      [3, 6, 9]], "Square matrix"
    assert transpose([[1, 4, 3],
                      [8, 2, 6],
                      [7, 8, 3],
                      [4, 9, 6],
                      [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                      [4, 2, 8, 9, 8],
                                      [3, 6, 3, 6, 1]], "Rectangle matrix"

    print("Use 'Check' to earn sweet rewards!")
