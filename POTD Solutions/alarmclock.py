'''
CodingBat Python Activity "alarm_clock" from logic-1.
codingbat.com
'''

failures = 0

def alarm_clock(day, vacation):
    '''
    Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat,
    and a boolean indicating if we are on vacation,
    return a string of the form "7:00" indicating when the alarm clock should ring.
    Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
    Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

    alarm_clock(1, False) → '7:00'
    alarm_clock(5, False) → '7:00'
    alarm_clock(0, False) → '10:00'
    '''
    if vacation == True:
        if 1<=day<=5:
            return "10:00"
        else:
            return "off"
    if 1<=day<=5:
        return "7:00"
    else:
        return "10:00"
    
    





def catchFailures(testCase, result):
    global failures
    
    try:
        assert eval(testCase) == result, "Test Case Failed: "+testCase+ " → "+str(result)
    except Exception as e:
        failures += 1
        print(e)
            


def test():
    global failures
    
    catchFailures("alarm_clock(1, False)", '7:00')
    catchFailures("alarm_clock(5, False)", '7:00')
    catchFailures("alarm_clock(0, False)", '10:00')
    catchFailures("alarm_clock(6, False)", '10:00')
    catchFailures("alarm_clock(0, True)", 'off')
    catchFailures("alarm_clock(6, True)", 'off')
    catchFailures("alarm_clock(1, True)", '10:00')
    catchFailures("alarm_clock(3, True)", '10:00')
    catchFailures("alarm_clock(5, True)", '10:00')

    if failures > 0:
        print("\r\n "+ str(failures) + " failed test case(s)   :(")
    else:
        print("Good job -- problem solved!")


test()