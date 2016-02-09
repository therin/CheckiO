
import math

def checkio (height, width):
    a, b = width / 2 , height / 2
    volume = 4 / 3 * math.pi * a ** 2 * b
    e = math.sqrt ( 1 - ( min (a, b) / max (a, b)) ** 2 )
    if a == b:
        surface_area = 4 * math.pi * a ** 2 
    elif a> b:
        surface_area = 2 * math.pi * (a ** 2 + b ** 2 * math.atanh (e) / e)
    else :
        surface_area = 2 * math.pi * (a ** 2 + a * b * math.asin (e) / e)
    return [ round (volume, 2 ), round (surface_area, 2 )]

'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
'''
print checkio(4, 2)
print checkio(2, 2)


