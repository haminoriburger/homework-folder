'''
CodingBat Python Activity "monkey_trouble" from warmup-1.
codingbat.com
'''

failures = 0

def monkey_trouble(a_smile, b_smile):
    '''
    We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
    We are in trouble if they are both smiling or if neither of them is smiling.
    Return True if we are in trouble.


    monkey_trouble(True, True) → True
    monkey_trouble(False, False) → True
    monkey_trouble(True, False) → False
    '''
    if a_smile == True and b_smile == True:
        return True
    if a_smile == False and b_smile == False:
        return True
    else:
        return False






def catchFailures(testCase, result):
    global failures
    
    try:
        assert eval(testCase) == result, "Test Case Failed: "+testCase+ " → "+str(result)
    except Exception as e:
        failures += 1
        print(e)
            


def test():
    global failures
    
    catchFailures('monkey_trouble(True, True)', True)
    catchFailures('monkey_trouble(False, False)', True)
    catchFailures('monkey_trouble(True, False)', False)
    catchFailures('monkey_trouble(False, True)', False)

    if failures > 0:
        print("\r\n "+ str(failures) + " failed test case(s)   :(")
    else:
        print("Good job -- problem solved!")


test()