'''
checkio([[
'X...',
'..X.',
'X..X',
'....'],[
'itdf',
'gdce',
'aton',
'qrdi']
]) == 'icantforgetiddqd'
 
checkio([[
'....',
'X..X',
'.X..',
'...X'],[
'xhwc',
'rsqx',
'xqzz',
'fyzr']
]) == 'rxqrwsfzxqxzhczy'
[[row[i] for row in matrix] for i in range(4)]

'''

def checkio(input_data):
    'Return password of given cipher map'
    cypher = input_data[0]
    text = input_data[1]
    answer = ""
    for turn in range(4):
        for r in range(len(cypher)):
            for i in range(len(cypher[r])):
                if cypher[r][i] == "X":
                    answer += text[r][i]
        #print answer
        cypher = zip(*cypher[::-1])
    return answer
 


print checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'],[
    'itdf',
    'gdce',
    'aton',
    'qrdi']])

#icantforgetiddqd'
