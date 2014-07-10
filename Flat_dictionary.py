# -*- coding: utf-8 -*-


def flatten(dictionary):
    stack = [[(), dictionary.copy()]]
    result = {}
    while stack:
        path, current = stack.pop()
        print path,current
        for k, v in current.items():
            print k,v
            if isinstance(v, dict):
                stack.append([path + (k,), v])
            else:
                result["/".join([path + (k,)])] = v
                
    if not result:
      result[k,] = v
    return result


'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
   # assert flatten({"key": "value"}) == {"key": "value"}, "Simple"

    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
'''
print flatten({"empty": {}})
#rint flatten_dict({"empty": {}})
#print unflatten({"empty": {}})

#print flatten({"name": {"first": "One","last": "Drone"},"job": "scout","recent": {},"additional": {"place": {"zone": "1","cell": "2"}}})
#assert flatten({"name": {"first": "One","last": "Drone"},"job": "scout","recent": {},"additional": {"place": {"zone": "1","cell": "2"}}}) == {"name/first": "One","name/last": "Drone","job": "scout","recent": "","additional/place/zone": "1","additional/place/cell": "2"}



