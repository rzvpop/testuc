from test import testAddAlarm, testDelayAlarm
from ui import *

def commandList():
    '''
        out: Returns dictionary with commands.
    '''
    cmds = {1: exit,
            2: help,
            3: uiAddAlarm,
            4: uiDelayAlarm,
            5: uiListAlarms}

    return cmds

def initAlarms(l):
    l.append(alarm(13, 2, 2, "Eat!"))
    l.append(alarm(14, 20, 0, "Sleep!"))
    l.append(alarm(13, 34, 2, "Wake up!"))
    l.append(alarm(17, 2, 2, "Sleep again!"))
    l.append(alarm(13, 2, 7, "Eat if money!"))

def test():
    testAddAlarm()
    testDelayAlarm()

def main():
    help()

    alarms = []
    commands = commandList()

    initAlarms(alarms)

    while True:
        cmd = input(">>")
        cmd = int(cmd)

        if cmd in commands:
            if cmd in [1, 2]:
                try:
                    commands[cmd]()
                except Exception as e:
                    print(e)
            else:
                try:
                    commands[cmd](alarms)
                except Exception as e:
                    print(e)

test()
main()
