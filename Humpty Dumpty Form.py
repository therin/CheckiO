
from math import pi 
def main(): 
    r = float(4) 
    v = r ** 3 * pi * 4 / 3 
    a = pi * 4 * r ** 2 
    print('The volume is %0.2f and the surface area is %0.2f' % (v, a)) 



def checkio(height, width):
    return [1, 1]




#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"


