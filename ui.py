from functionalities import *

def help():
    '''
        Prints menu list.
    '''
    lst = ""
    lst += "1-Exit\n"
    lst += "2-Help\n"
    lst += "3-Add alarm\n"
    lst += "4-Delay alarm\n"
    lst += "5-List alarms\n"

    print(lst)

def uiAddAlarm(l):
    h = input("hour: ")
    m = input("minute: ")
    s = input("second: ")
    desc = input("description: ")
    args = [h, m, s, desc]

    addAlarm(l, args)
    print("Alarm added!")

def uiDelayAlarm(l):
    print("Alarm:\n")
    h1 = input("hour: ")
    m1 = input("minute: ")
    s1 = input("second: ")
    print("\nDelay until:\n")
    h2 = input("hour: ")
    m2 = input("minute: ")
    s2 = input("second: ")

    args = [h1, m1, s1, h2, m2, s2]

    delayAlarm(l, args)
    print("Alarm delayed!")

def uiListAlarms(l):
    str = alarmStr(l)
    print(str)