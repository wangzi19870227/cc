import functools


def log(func):
    # should run this, or outside myfunc.__name__ will return '_deco'
    @functools.wraps(func)
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco

def log_with_args(text):
    def _wrap(func):
        # should run this, or outside myfunc.__name__ will return '_deco'
        @functools.wraps(func) 
        def _deco(*args, **kwargs):
            print("before %s %s called." % (text, func.__name__))
            ret = func(*args, **kwargs)
            print("  after %s %s called. result: %s" % (text, func.__name__, ret))
            return ret
        return _deco
    return _wrap

@log
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a+b

@log_with_args('excute')
def myfunc2(a, b):
    print(" myfunc2(%s,%s) called." % (a, b))
    return a+b

myfunc(1, 2)
print myfunc.__name__

myfunc2(1, 2)
print myfunc2.__name__
