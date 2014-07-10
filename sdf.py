
'''
foos = [1,2,3,4,5]

result = 0
def maptest(foo):
    global result
    result +=foo

map(maptest, foos)
print result
'''

result = 0
result1 = 0
def checkio(data):
    global result
    def maptest(foo):
        global result
        result +=foo
        print 'adding ' + str(foo) + ' to ' + str(result)
    map(maptest, data)
    result1 = result
    result = 0
    return result1