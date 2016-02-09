def decode_amsco(message, key):
    return message

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco(u"oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco(u'kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco(u'hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
