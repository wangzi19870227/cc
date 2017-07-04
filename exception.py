def my_ex():
    raise

try:
    my_ex()
except Exception as ex:
    print ex
