import traceback


class BaseModelException(Exception):
    def __str__(self):
        return self.message


class TimeFormatError(BaseModelException):
    def __init__(self, time):
        self.time = time
        self.message = 'time (%s) format error! ISO8601 format required.' % time


class ResourceAlreadyExistError(BaseModelException):
    def __init__(self, resource_id):
        self.resource_id = resource_id
        self.message = 'resource id (%s) already exist.' % resource_id


def aaa():
    raise TimeFormatError('xxx')


def bbb():
    raise ResourceAlreadyExistError('xxx')


def re_raise():
    e = None
    for i in (1,2):
        try:
            aaa()
        except Exception as e:
            stack = traceback.format_exc()
            print '[ERROR] aaa error! %s' % e
 
    # Notice:
    # 1) If no expressions are present after raise, raise re-raises the last Exception
    #    that was active in the current scope.
    # 2) If no Exception is active in the current scope, a TypeError Exception is raised
    #    indicating that this is an error.
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
    
    # Notice:
    # 1) If no expressions are present after raise, raise re-raises the last Exception
    #    that was active in the current scope.
    # 2) If no Exception is active in the current scope, a TypeError Exception is raised
    #    indicating that this is an error.
    if e is not None:
        print('[ERROR] aaa/bbb done with error! last error: %s. last traceback: %s' % (e, stack))
        #raise e # if you want re-raise Expection, do not raise e. only when you want hide this !
        raise


re_raise()
re_raise_the_last_ex()

