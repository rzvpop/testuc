from domain import alarm
from functionalities import addAlarm, delayAlarm


def testAddAlarm():
    l = []
    args = ["15", "45", "12", "Eat!"]
    a = alarm(15, 45, 12, "Eat!")

    addAlarm(l, args)

    assert(l[0] == a)

def testDelayAlarm():
    l = []
    a1 = ["15", "45", "12", "Wake up!"]
    a2 = ["7", "39", "12", "Comb your hair!"]
    a3 = ["5", "23", "0", "Put a little make up!"]

    addAlarm(l, a1)
    addAlarm(l, a2)
    addAlarm(l, a3)

    args = ["15", "45", "12", "16", "0", "0"]

    #delayAlarm(l, args)

    #assert(l[0]["time"] == (16, 0, 0))