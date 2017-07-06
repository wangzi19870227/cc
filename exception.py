import traceback


class MyException(Exception):
    pass


class MyException2(Exception):
    pass

def aaa():
    raise MyException('xxx')

def bbb():
    raise MyException('yyy')

def re_raise():
    e = None
    for i in (1,2):
        try:
            aaa()
        except Exception as e:
            stack = traceback.format_exc()
            print '[ERROR] aaa error! %s' % e
 
    if e is not None:
        print('[ERROR] aaa done with error! last error: %s. last traceback: %s' % (e, stack))
        #raise e # if you want re-raise Expection, do not raise e. only when you want hide this !
        raise

def re_raise_the_last_ex():
    e = None
    try:
        aaa()
    except Exception as e:
        stack = traceback.format_exc()
        print '[ERROR] aaa error! %s' % e
    
    try:
        bbb()
    except Exception as e:
        stack = traceback.format_exc()
        print '[ERROR] bbb error! %s' % e
    
    if e is not None:
        print('[ERROR] aaa/bbb done with error! last error: %s. last traceback: %s' % (e, stack))
        #raise e # if you want re-raise Expection, do not raise e. only when you want hide this !
        raise


re_raise()
re_raise_the_last_ex()

