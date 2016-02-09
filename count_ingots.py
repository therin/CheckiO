import string

def count_ingots(report):

    splitted = report.split(',')
    result = 0
    for A,B in splitted:
    	#print "looking at " + A,B
    	item = string.uppercase.index(A) + 1
#    	print item
    	if item == 1:
    		result += int(B)
    		#print int(B)
    	else:
	    	#print 9 * (item-1) + int(B)
    		result += 9 * (item-1)  + int(B)
    return result


if __name__ == '__main__':
    # These "asserts" are used only for self-checking and not necessary for auto-testing
    assert count_ingots("A2,B1") == 12, "One and eleven"
    assert count_ingots("A1,A1,A1") == 3, "One, two, three"
    assert count_ingots("Z9,X8,Y7") == 672, "XYZ"
    assert count_ingots("C1,D1,B1,E1,F1") == 140, "Daily normal"


print count_ingots("A2,B1")