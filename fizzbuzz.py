def fizz_buzz(number):
    if not number % 3 and not number % 5:
        return "Fizz Buzz"
    elif not number % 3:
        return "Fizz"
    elif not number % 5:
        return "Buzz"
    elif number % 3 and number % 5:
        return number





#if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert fizz_buzz(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
#    assert fizz_buzz(6) == "Fizz", "6 is divisible by 3"
#    assert fizz_buzz(5) == "Buzz", "5 is divisible by 5"
#    assert fizz_buzz(7) == "7", "7 is not divisible by 3 or 5"

print fizz_buzz(15)
print fizz_buzz(6)
print fizz_buzz(5)
print fizz_buzz(7)