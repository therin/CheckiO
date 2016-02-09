# -*- coding: utf-8 -*-
'''
URL normalization is the process by which URLs are modified and standardized in a consistent manner. The goal of the normalization process is to transform a URL into a normalized or canonical URL so it is possible to determine if two syntactically different URLs may be equivalent.

For our normalization we will use normalizations that preserve semantics. You should normalize a given url using the next rules (only these rules. They are slightly different from RFC).

Normalization Rules:
1. Converting the scheme and host to lower case.
HTTP://www.Example.com/ → http://www.example.com/
2. Capitalizing letters in escape sequences. All letters within a percent-encoding triplet (e.g., "%3B") are case-insensitive, and should be capitalized.
http://www.example.com/a%c2%b1b → http://www.example.com/a%C2%B1b
3. Decoding percent-encoded octets of unreserved characters. For consistency, percent-encoded octets in the ranges of ALPHA (%41–%5A and %61–%7A), DIGIT (%30–%39), hyphen (%2D), period (%2E), underscore (%5F), or tilde (%7E) should not be created by Uniform Resource Identifiers (URI) producers and, when found in a URI, should be decoded to their corresponding unreserved characters by URI normalizers.
http://www.example.com/%7Eusername/ → http://www.example.com/~username/
4. Removing the default port. The default port (port 80 for the “http” scheme) should be removed from a URL.
http://www.example.com:80/bar.html → http://www.example.com/bar.html
5. Removing dot-segments. The segments “..” and “.” can be removed from a URL according to the algorithm described in RFC 3986 (or a similar algorithm). ".." is a parent directory, "." is the same directory.
http://www.example.com/a/b/../c/./d.html → http://www.example.com/a/c/d.html
Additional links: If you are interested to know more about URL normalization (This is not necessarily for this task), then you can find more information here: Wikipedia, RFC3986
Input: URL, an unicode string.

checkio("Http://Www.Checkio.org") == "http://www.checkio.org"
checkio("http://www.checkio.org/%cc%b1bac") == "http://www.checkio.org/%CC%B1bac"
checkio("http://www.checkio.org/task%5F%31") == "http://www.checkio.org/task_1"
checkio("http://www.checkio.org:80/home/") == "http://www.checkio.org/home/"
checkio("http://www.checkio.org:8080/home/") == "http://www.checkio.org:8080/home/"
checkio("http://www.checkio.org/task/./1/../2/././name") == "http://www.checkio.org/task/2/name"
How it is used: This concept will help you in parsing and analytical processing. URL normalization is required if you need to compare the various URL addresses or you are running a system where letter-casing is sensitive.

Precondition: All input urls are valid.
'''
import re
from string import ascii_letters

def remove_dot_segments(path):
    dirs = []
    for d in path.split('/'):
        if d == '.':
            continue
        elif d == '..':
            if dirs:
                dirs.pop()
        else:
            dirs.append(d)
    return '/'.join(dirs)

def percent_decode(s, encoding='utf-8', decodable=None):
    mychr = chr
    list_ = s.split('%')
    res = [list_[0]]
    myappend = res.append
    del list_[0]
    for item in list_:
        if item[1:2]:
            try:
                c = mychr(int(item[:2], 16))
                if decodable is None:
                    myappend(c + item[2:])
                elif c in decodable:
                    myappend(c + item[2:])
                else:
                    myappend('%' + item)
            except ValueError:
                myappend('%' + item)
        else:
            myappend('%' + item)
    s = ''.join(res)
    return s

def normalize_octets(match):
    s = match.group()
    i = int(s[1:], 16)
    if 0x41 <= i <= 0x5A or 0x61 <= i <= 0x7A or 0x30 <= i <= 0x39 or i in [0x2D, 0x2E, 0x5F, 0x7E]:
        return chr(i).lower()
    else:
        return s.upper()

def checkio(url):

    rule1 = url.lower()
    rule2 = re.sub("(?i)%[0-9A-F]{2}", lambda x: x.group(0).upper(), rule1)
    rule3 = percent_decode(rule2, decodable='0123456789%s-._~' % ascii_letters)
    url_pattern = re.compile(r'^(.+?)://(.+?)?(:\d+)?(/.*)?$')
    scheme, host, port, path = [s or '' for s in url_pattern.match(rule3).groups()]
    if (scheme, port) == ('http', ":80"):
        port = ''
    path = remove_dot_segments(path)
    scheme = scheme.lower()
    path_pattern = re.compile(r'(%[\da-f]{2})', re.I)
    path = path_pattern.sub(normalize_octets, path.lower())
    rule45 = '{}://{}{}{}'.format(scheme, host, port, path)
    return rule45

print checkio(u"Http://Www.Checkio.org")

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio(u"http://www.checkio.org/%cc%b1bac") ==\
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio(u"http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio(u"http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio(u"http://www.checkio.org:8080/home/") == \
        "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio(u"http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')

print checkio(u"http://www.checkio.org:80/home/")