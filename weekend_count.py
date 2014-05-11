from datetime import date
import datetime

def checkio(from_date, to_date):
    counter = 0
    diff = to_date - from_date
    for i in range(diff.days + 1):
        #print (from_date + datetime.timedelta(i)).isoformat()
        if (datetime.datetime.strptime((from_date + datetime.timedelta(i)).isoformat(), '%Y-%m-%d')).isoweekday() == 6 or \
        (datetime.datetime.strptime((from_date + datetime.timedelta(i)).isoformat(), '%Y-%m-%d')).isoweekday() == 7:
            counter +=1
    return counter

#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

