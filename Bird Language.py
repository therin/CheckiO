# -*- coding: utf-8 -*-

'''
Stephan has a friend who happens to be a little mechbird. Recently, he was trying to teach it how to speak basic language. Today the bird 
spoke its first word: "hieeelalaooo". This sounds a lot like "hello", but with too many vowels. Stephan asked Nikola for help and he helped
 to examine how the bird changes words. With the information they discovered, we should help them to make a translation module.

The bird converts words by two rules:
- after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Vowels letters == "aeiouy".

You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one whitespace).
 The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given in lowercase. You should 
 translate this phrase from the bird language to something more understandable.

Input: A bird phrase as a string.

Output: The translation as a string.

Exa
translate("hieeelalaooo") == "hello"
translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
translate("aaa bo cy da eee fe") == "a b c d e f"
translate("sooooso aaaaaaaaa") == "sos aaa"
How it is used: This a similar cipher to those used by children when they invent their own "bird" language. Now you will be ready to
 crack the code.

Precondition: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
A phrase always has the translation.
'''

VOWELS = "aeiouy"

def translate(phrase):
  result = []
  def oneword(word):
      #print "working with " + w
      counter = 0
      work = word
      answer = []
      for i in range(len(work)):
        if i < counter:
          #print "skipping " + work[i]
          pass
        else:
          if work[i] in VOWELS:
            answer.append(work[i])
            #print 'adding ' + work[i]
            counter += 3
          else:
            answer.append(work[i])
            #print 'adding ' + work[i]
            counter +=2
      return ''.join(answer)
  for word in phrase.split(' '):
    print word
    result.append(oneword(word))
  return " ".join(result)



'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate(u"hieeelalaooo") == "hello", "Hi!"
    assert translate(u"hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate(u"aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate(u"sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
'''
print translate(u"hoooowe yyyooouuu duoooiiine")

