# default args must be mmutable, but here L is changeable L=[], will lead
# to logical error
def add_end_error(L=[]):
    L.append('END')
    return L

# default args is mmutable L=None, ok
def add_end_ok(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# test error case
print add_end_error()
print add_end_error()
print add_end_error()

# test ok case
print add_end_ok()
print add_end_ok()
print add_end_ok()
