'''
CodingBat Python Activity "sleep_in" from warmup-1.
codingbat.com
'''

failures = 0

def sleep_in(weekday, vacation):
    '''
    The parameter weekday is True if it is a weekday,
    and the parameter vacation is True if we are on vacation.
    We sleep in if it is not a weekday or we're on vacation.
    Return True if we sleep in.


    sleep_in(False, False) → True
    sleep_in(True, False) → False
    sleep_in(False, True) → True
    '''
    if vacation == True:
        return True
    else:
        if weekday == True:
          return False
        else:
            return True



def catchFailures(testCase, result):
    global failures
    
    try:
        assert eval(testCase) == result, "Test Case Failed: "+testCase+ " → "+str(result)
    except Exception as e:
        failures += 1
        print(e)
            


def test():
    global failures
    
    catchFailures('sleep_in(False, False)', True)
    catchFailures('sleep_in(True, False)', False)
    catchFailures('sleep_in(False, True)', True)
    catchFailures('sleep_in(True, True)', True)

    if failures > 0:
        print("\r\n "+ str(failures) + " failed test case(s)   :(")
    else:
        print("Good job -- problem solved!")


test()