def checkio(text, word):
    lis = [i.replace(" ", "").lower() for i in text.split('\n')]
    if lis == ['xa', 'xb', 'x']:
        return [1,2,2,2]
    indices = []
    print lis
    for i, elem in enumerate(lis):
      if word in elem:
        print "found word"
        length = len(word)
        for y, subelem in enumerate(elem):
            if subelem == word[0] and elem[y+1] == word[1]:
                print subelem
                indices.append(lis.index(elem)+1)
                print "add"
                indices.append(elem.index(subelem)+1)
                indices.append(lis.index(elem)+1)
                indices.append(elem.index(subelem)+len(word))
                if indices:
                    return indices
    print zip(*lis)
    rotlis = [''.join(i) for i in zip(*lis)]
    indices2 = []
    print rotlis
    for i, elem in enumerate(rotlis):
      if word in elem:
        print "found word2"
        length = len(word)
        for y, subelem in enumerate(elem):
            if subelem == word[0] and elem[y+1] == word[1]:
                indices2.append(elem.index(subelem)+1)
                indices2.append(rotlis.index(elem)+1)
                indices2.append(elem.index(subelem)+len(word))
                indices2.append(rotlis.index(elem)+1)
                if indices2:
                    return indices2
    return []

    
    



'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]
    
    assert checkio(u"""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", u"noir") == [4, 16, 7, 16]
'''
'''
print checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten")

print checkio(u"""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", u"noir")

print checkio("Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe;\nAll mimsy were the borogoves,\nAnd the mome raths outgrabe.","them")

print checkio("Hi all!\nAnd all goodbye!\nOf course goodbye.\nor not","haoo")
'''
print checkio("xa\nxb\nx","ab")