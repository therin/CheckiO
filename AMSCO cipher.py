def decode_amsco(message, key):
    one = True
    matrix = []
    for item in str(key):
        matrix.append([item])
    some = list(message)
    while some:
        for number in matrix:
            if one and len(some) > 0:
                item = some.pop(0).encode('ascii', 'ignore')
                number.append(item)
                one = False
                item = ''
            elif not one and len(some) > 1:
                item = some.pop(0).encode('ascii', 'ignore') + some.pop(0).encode('ascii', 'ignore')
                number.append(item)
                one = True
                item = ''
            elif not one and len(some) == 1:
                item = some.pop(0).encode('ascii', 'ignore')
                number.append(item)
                one = False
                item = ''
        one = not one
    #print matrix
    maximum = len(matrix[1])-1
    hard_maximum = maximum
    one = False
    matrix = []
    for item in str(key):
        matrix.append([item])
    matrix.sort()
    some1 = list(message)
    while some1:
        for number in matrix:
            while hard_maximum > 0:
                if one and len(some1) > 0:
                    item = some1.pop(0).encode('ascii', 'ignore')
                    number.append(item)
                    one = False
                    item = ''
                elif not one and len(some1) > 1:
                    item = some1.pop(0).encode('ascii', 'ignore') + some1.pop(0).encode('ascii', 'ignore')
                    number.append(item)
                    one = True
                    item = ''
                elif not one and len(some1) == 1:
                    item = some1.pop(0).encode('ascii', 'ignore')
                    number.append(item)
                    one = False
                    item = ''
                hard_maximum -= 1
            one = not one
            hard_maximum = maximum
    print matrix
   

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco(u"oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco(u'kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco(u'hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
