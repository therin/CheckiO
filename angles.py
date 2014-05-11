import math

def checkio(a, b, c):
    def angle (a, b, c):
        try:
            return math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b)))
        except Exception, e:
            return 0

    angA = int(round(angle(b,c,a)))
    angB = int(round(angle(c,a,b)))
    angC = int(round(angle(a,b,c)))

    return [angA,angB,angC]


    #replace this for solution
    return [0, 0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

'''
    angA = int(angle(b,c,a))
    angB = int(angle(c,a,b))
    angC = int(angle(a,b,c))
    '''