# -*- coding: utf-8 -*-
'''
Nicola believes that Sophia calls to Home too much and her phone bill is much too expensive. He took the bills for Sophia's calls from the last
few days and wants to calculate how much it costs.

The bill is represented as an array with information about the calls. Help Nicola to calculate the cost for each of Sophia calls. Each call is 
represented as a string with date, time and duration of the call in seconds in the follow format:
"YYYY-MM-DD hh:mm:ss duration"
The date and time in this information are the start of the call.
Space-Time Communications Co. has several rules on how to calculate the cost of calls:

First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
After 100 minutes in one day, each minute costs 2 coins per minute;
All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min, 61 sec ≈ 2 min;
Calls count on the day when they began. For example if a call was started 2014-01-01 23:59:59, then it counted to 2014-01-01;
For example:

2014-01-01 01:12:13 181
2014-01-02 20:11:10 600
2014-01-03 01:12:13 6009
2014-01-03 12:13:55 200
First day -- 181s≈4m -- 4 coins;
Second day -- 600s=10m -- 10 coins;
Third day -- 6009s≈101m + 200s≈4m -- 100 + 5 * 2 = 110 coins;
Total -- 124 coins.
Input: Information about calls as a tuple of strings.

Output: The total cost as an integer.

Example:

total_cost(("2014-01-01 01:12:13 181",
            "2014-01-02 20:11:10 600",
            "2014-01-03 01:12:13 6009",
            "2014-01-03 12:13:55 200")) == 124
How it is used: This mission will teach you how to parse and analyse various types data. Sometimes you don't need the full data and should single out
only important fragments.

Precondition: 0 < len(calls) ≤ 30
0 < call_duration ≤ 7200
The bill is sorted by datetime.
'''
import math
import datetime
import time
#from datetime import datetime
#from datetime import timedelta


def total_cost(calls):

    def same_day(duration):
        total = 0
        if duration <= 100:
            print "Same Day, added " + str(duration)
            return duration
        else:
            total += 100
            duration = duration - 100
            total += duration*2
            print "Same Day, added " + str(total)
            return total

    def another_day(duration):
        print "Another Day, added " + str(duration*2)
        return duration*2
        

    split = []
    time = []
    last_time = []
    rlt = []
    total = []
    cost = 0
    for call in calls:
        split_call = call.split(" ") 
        split.append(split_call)
    for item in split:
        time.append(str(item[0]+ " " +item[1]))
    #print time
    for item in time:
        dt_obj = datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')
        last_time.append(dt_obj)
    #print last_time
    for i in range(len(last_time)):
        rlt.append((last_time[i],split[i][2]))
    sameday = False
    print rlt
    for i in range(len(rlt)):
        #print int(rlt[i][1])/60.0
        if same_day:
            total.append(same_day(int(math.ceil(int(rlt[i][1])/60.0))))
            try:
                if rlt[i][0].date() == rlt[i+1][0].date():
                    sameday = False
                else:
                    sameday = True
            except Exception, e:
                print e
                pass
        else:
            total.append(another_day(int(math.ceil(int(rlt[i][1])/60.0))))
            try:
                if rlt[i][0].date() == rlt[i+1][0].date():
                    sameday = False
                else:
                    sameday = True
            except Exception, e:
                print e
                pass
    print sum(total)
    return sum(total)
            
'''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost((u"2014-02-05 01:00:00 60",
                       u"2014-02-05 02:00:00 60",
                       u"2014-02-05 03:00:00 60",
                       u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"

'''


total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200"))


total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1"))