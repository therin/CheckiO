# -*- coding: utf-8 -*-
'''
In a correctly designed system, a plain password is not stored in the database. Instead, a hash of the password is stored. You are 
going to verify a password and you will need to use the same one-way function to calculate the hash and do a comparison.

Input: Two arguments. A string to be hashed and a hash algorithm as a string (unicode utf8).

Output: Hexadecimal hash for for input string using given algorithm as a string.

2
checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86bhe3d7'
checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
Precondition:
algorithm in ("md5", "sha224", "sha256", "sha384", "sha512", "sha1")
0 ≤ len(hashed_string) ≤ 2**10
'''
'''
import hashlib
def checkio(hashed_string, algorithm):
    h = hashlib.new(algorithm)
    h.update(hashed_string)
    return h.hexdigest()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio(u'happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
'''





import base64
coded_string = '3gWy+O2UzcctP/URbfvTfw=='
print base64.b64decode(coded_string)