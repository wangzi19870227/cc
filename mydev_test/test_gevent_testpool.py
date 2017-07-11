#from gevent import monkey
#monkey.patch_socket()
import gevent
import datetime
import traceback
import signal
from gevent.event import Event
from gevent.pool import Pool

stop_event = Event()


def signal_handler():
    stop_event.set()


def do_job(func, interval):
    while True:
        start_time = datetime.datetime.utcnow()
        print("do_job() start. gevent: %s, time: %s, func: %s" % 
              (gevent.getcurrent(), start_time, func.func_name))
        try:
            func(interval)
        except:
            stack = traceback.format_exc()
            print('stack: %s' % stack)
        else:
            end_time = datetime.datetime.utcnow()
            consume = (end_time - start_time).seconds
            print('do_job() OK. gevent: %s, time: %s, func: %s, consume: %s' %
                  (gevent.getcurrent(), end_time, func.func_name, consume))
        finally:
            print('do_job() done.')
            gevent.sleep(interval)
            print('do_job() do next.')

def hello(interval):
    print('hello ...')
    #import time
    #time.sleep(3)
    print('hello.')

    raise Exception('error: xxx')

def send_metering(interval):
    #pass
    print('send_metering...')
    print('send_metering.')

def handle_metering_error(interval):
    #pass
    print('handle_metering_error ...')
    print('handle_metering_error.')

def run():
    pool = Pool()
    gevent.signal(signal.SIGQUIT, signal_handler)
    gevent.signal(signal.SIGTERM, signal_handler)
    gevent.signal(signal.SIGINT, signal_handler)

    print('run(), start.')

    #gevent.joinall([
    #    gevent.spawn(do_job, hello, 1),
    #    gevent.spawn(do_job, send_metering, 10),
    #    gevent.spawn(do_job, handle_metering_error, 5),
    #])

    pool.spawn(do_job, hello, 1),
    pool.spawn(do_job, send_metering, 10),
    pool.spawn(do_job, handle_metering_error, 5),
    pool.join()
    #pool.join(timeout=10)

    #if stop_event.wait(timeout=10):
    #    pool.kill(block=True)
    #    pool.join(timeout=10)
    
    print('run(), OK.')

run()

