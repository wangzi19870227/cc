from threading import Timer  
import time  
  
def wait_callback():  
    print 'callback running'  
    global timer
    timer = Timer(3, wait_callback)
    timer.start()
  
timer = Timer(1, wait_callback)  
timer.start()  
