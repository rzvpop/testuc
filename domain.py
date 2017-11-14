def alarm(h, m, s, desc):
    '''
        Returnes an alarm object.
        in: h(int), m(int), s(int), desc(descpription-string)
        out: alarm(a dictionary with a tuple and a string)
    '''
    return {"time": (h, m, s), "desc": desc}

def testAlarm():
    a = alarm(9, 30, 0, "You should hurry up!")
    assert(a == {"time": (9, 30, 0), "desc": "You should hurry up!"})

testAlarm()