# -*- coding: utf-8 -*-

def flat_list(array):
  i = array
  if isinstance(i, list):
    return [a for i in i for a in flat_list(i)]
  else:
    return [i]



print flat_list([1,2,3])


