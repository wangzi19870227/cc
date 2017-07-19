import datetime
import time

def local2utc(local_dt):
    print('---------local_dt:%s' % local_dt)
    time_struct = time.mktime(local_dt.timetuple())
    print('---------time_struct:%s' % time_struct)
    utc_dt = datetime.datetime.utcfromtimestamp(time_struct)
    print('---------utc_dt:%s' % utc_dt)
    return utc_dt

local_dt = datetime.datetime(2016,07,07,22,00,00)
utc_dt = local2utc(local_dt)
print('local_dt:%s, utc_dt:%s' % (local_dt, utc_dt))
