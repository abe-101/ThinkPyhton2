#!/usr/bin/python3

#wrong the function loop will run only once
def any_lower1(s):
    for c in s:
        print(c)
        if c.islower():
            return True
        else:
            return False

#wrong the function loop will run only once
#just do with 'c',always True ,and True is string,not bool
def any_lower2(s):
    for c in s:
        print(c)
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

#wrong if string end with a UP ,will always be False
def any_lower3(s):
    for c in s:
        print(c)
        flag = c.islower()
    return flag

#right
def any_lower4(s):
    flag=False
    for c in s:
        flag=flag or c.islower()
    return flag

#wrong,if it find a UPletter ,everything will get an F
def any_lower5(s):
    for c in s:
        if not c.islower():
            return False
    return True

test='Hello_World'
uptest="ASSbDF"
#print(any_lower3(test),type(any_lower3(test)))
print(any_lower4(uptest))
