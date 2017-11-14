from domain import alarm
from validator import validate
from utils import add

def addAlarm(l, args):
    '''
        Adds alarm in list of alarms.
        in: l(list of alarms), args(parameters of the alarm)
    '''
    a = alarm(int(args[0]), int(args[1]), int(args[2]), args[3])
    validate(a)
    add(l, a)

def findAlarm(l, a):
    '''
        Finds alarm in list.
        in: l, a
        out: index of alarm if it exists, False if it doesn't
    '''
    for i in range(len(l)):
        if a["time"] == l[i]["time"]:
            return i
    return False

def delayAlarm(l, args):
    '''
        Changes the time of an alarms.
        in: h1, m1, s1 - original time of the alarm; h2, m2, s2 - new time
        It raises exception if alarm isn't in the list or if the new time is less then the original
    '''
    a = alarm(int(args[0]), int(args[1]), int(args[2]), "default")
    validate(a)
    idx = findAlarm(l, a)

    if idx == False:
        raise Exception("Not in list!\n")
    else:
        l[idx]["time"][0] = int(args[3])
        l[idx]["time"][1] = int(args[4])
        l[idx]["time"][2] = int(args[5])

        if l[idx]["time"] < a["time"]:
            raise Exception("New time can't be new time is less then the original time!\n")

def alarmStr(l):
    strg = ""

    for x in l:
        strg += str(x["time"][0]) + ":" + str(x["time"][1]) + ":" + str(x["time"][2]) + "  " + x["desc"] + "\n"

    return strg