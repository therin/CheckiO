# -*- coding: utf-8 -*-

def golf(password):
    p = password
    return len(p)>=10 and any(i.isdigit() for i in p) and any(i.islower() for i in p) and any(i.isupper() for i in p)

print golf('Aaaaa1')
#print golf('A1213pokl') == False
#print golf('bAse730onE') == True
#print golf('asasasasasasasaas') == False
#print golf('QWERTYqwerty') == False
#print golf('123456123456') == False
#print golf('QwErTy911poqqqq') == True
