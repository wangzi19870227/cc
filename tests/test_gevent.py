from gevent import monkey; monkey.patch_socket()
import gevent


def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        #raise Exception('xxx')
        gevent.sleep(0)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
print 'gevents spawn done.'

g1.join()
g2.join()
g3.join()
print'gevents join done.'
