from threading import Timer  
import datetime  
  
def t1_run():  
    print 'running t1, time: %s' % datetime.datetime.now()  
  
def t2_run():  
    print 'running t2, time: %s' % datetime.datetime.now()  
  
def t1():
    t=Timer(1,t1_run)  
    t.start()  

def t2():
    t=Timer(5,t2_run)  
    t.start()  

print('call t1, time: %s' % datetime.datetime.now())
t1()
print('call t2, time: %s' % datetime.datetime.now())
t2()
