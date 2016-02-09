# -*- coding: utf-8 -*-



def checkio(number):
    lis = [i * (i + 1) / 2 for i in range(50)][1:]
    print lis
    result = []
    sum1 = 0
    for i in range(len(lis)):      
      counter = i
      while counter < len(lis):
        sum1 += lis[counter]
        result.append(lis[counter])
        if sum1 == number:
          return result
        counter +=1
      counter = 0
      sum1 = 0
      result = []
    return []







'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
'''

print checkio(10)