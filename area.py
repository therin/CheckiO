
num='5'
def area(num):
    if '.' in num:
        num = float(num)
    else:
        num = int(num)
    return num**2
    
print area(num)