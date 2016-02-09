

import math


def checkio(opacity):
    def is_fibonacci(n):
        phi = 0.5 + 0.5 * math.sqrt(5.0)
        a = phi * n
        return n == 0 or abs(round(a) - a) < 1.0 / n

    test_o = 10000
    for x in range(0, 5000):
    	if is_fibonacci(x):
    		test_o -= x
    	else:
    		test_o += 1
    	if test_o == opacity:
    		print x
    		return x



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
