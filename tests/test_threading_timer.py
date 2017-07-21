from threading import Timer  
import datetime
import time


def do_action(timer_name):
    print 'timer %s running do_action, time: %s' % (timer_name,
            datetime.datetime.now())
    raise Exception('xxx')

def cycle_timer(interval, wait_call_back, args):  
    # do action
    try:
        wait_call_back(args)
    except Exception as e:
        print 'ERROR: %s' % e

    # go next timer
    global timer
    timer = Timer(interval, cycle_timer, (interval, wait_call_back, args))
    timer.start()

# test once timer
# Notice: ('t1', ), not ('t1'), or it will be consider as ('t', '1')
print('start timer t1(once timer), time: %s' % datetime.datetime.now())
t1=Timer(2, do_action, ('t1',)) 
t1.start()  
print('start timer t2(once timer), time: %s' % datetime.datetime.now())
t2=Timer(4, do_action, ('t2',))  
t2.start()  

# test once timer timeout
TIMEOUT=3
time.sleep(TIMEOUT)
print('timeout %s reached, cancel all' % TIMEOUT)
t1.cancel()
t2.cancel()
print('end')

# test cycle timer
DELAY=5
print('start timer t3(cycle timer), time: %s' % datetime.datetime.now())
t3 = Timer(DELAY, cycle_timer, (2, do_action, 't3'))
t3.start()
print('start timer t4(cycle timer), time: %s' % datetime.datetime.now())
t4 = Timer(DELAY, cycle_timer, (4, do_action, 't4'))
t4.start()  

