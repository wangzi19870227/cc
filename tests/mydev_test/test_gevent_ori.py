from gevent import monkey; monkey.patch_socket()
import gevent

def f1(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(1)

def f2(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(5)

while True:
    g1 = gevent.spawn(f1, 5)
    g2 = gevent.spawn(f2, 5)
    g1.join()
    g2.join()
