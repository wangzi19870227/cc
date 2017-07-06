import datetime
import time

ISO8601_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
LOCAL_FORMAT = '%Y-%m-%d %H:%M:%S'


###########################
# datetime <-> string
###########################
def format_iso8601(date):
    return datetime.datetime.strftime(date,
                                      ISO8601_FORMAT)


def parse_iso8601(date_str):
    return datetime.datetime.strptime(date_str,
                                      ISO8601_FORMAT)


def format_local(date):
    return datetime.datetime.strftime(date,
                                      LOCAL_FORMAT)


def parse_local(date_str):
    return datetime.datetime.strptime(date_str,
                                      LOCAL_FORMAT)


###########################
# datetime local <-> utc
###########################
def local2utc(local_dt):
    time_struct = time.mktime(local_dt.timetuple())
    utc_dt = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_dt


###########################
# datetime <-> timestamp
###########################
def datetime2timestamp(dt, convert_to_utc=False):
    """ Converts a datetime object to UNIX timestamp in milliseconds. """
    # if isinstance(dt, datetime.datetime):
    #     if convert_to_utc:
    #         dt = dt + datetime.timedelta(hours=-8)
    #     timestamp = (dt - EPOCH).total_seconds()
    #     return long(timestamp)
    # return dt

    return int(time.mktime(dt.timetuple()))


def timestamp2datetime(timestamp, convert_to_local=True):
    """ Converts UNIX timestamp to a datetime object. """
    # if isinstance(timestamp, (int, long, float)):
    #     dt = datetime.datetime.utcfromtimestamp(timestamp)
    #     if convert_to_local:
    #         dt = dt + datetime.timedelta(hours=8)
    #     return dt
    # return timestamp

    if isinstance(timestamp, (int, long, float)):
        if convert_to_local:
            dt = datetime.datetime.fromtimestamp(timestamp)
        else:
            dt = datetime.datetime.utcfromtimestamp(timestamp)
        return dt
    return timestamp


###########################
# datetime now/utcnow & 
# timestamp now/utcnow
###########################
def datetime_now():
    return datetime.datetime.now()


def datetime_utc_now():
    return datetime.datetime.utcnow()


def timestamp_now():
    # return str(time.time()).split('.')[0]
    return datetime2timestamp(datetime_now())


def timestamp_utc_now():
    return datetime2timestamp(datetime_utc_now())


if __name__ == '__main__':
    # test datetime <-> timestamp, for now
    dt_now = datetime_now()
    ts_now = timestamp_now()
    print('datdtime now: %s' % dt_now)
    print('timestamp now: %s' % ts_now)
    print('timestamp2datetime: %s' % timestamp2datetime(ts_now))
    print('datetime2timestamp: %s' % datetime2timestamp(dt_now))

    # test datetime <-> timestamp, for utcnow
    dt_utcnow = datetime_utc_now()
    ts_utcnow = timestamp_utc_now()
    print('datetime utc now: %s' % dt_utcnow)
    print('timestamp utc now: %s' % ts_utcnow)
    print('timestamp2datetime: %s' % timestamp2datetime(ts_utcnow))
    print('datetime2timestamp: %s' % datetime2timestamp(dt_utcnow))

    # test local <-> utc
    dt_now = datetime_now()
    dt_utcnow = local2utc(dt_now)
    print('dt now: %s, converted to dt utc now: %s' % (dt_now, dt_utcnow))
    dt_utcnow = datetime_utc_now()
    print('real dt utc now: %s' % dt_utcnow)

    # test datetime <-> string 
    dt_now = datetime_now()
    str_now = format_iso8601(dt_now)
    print('datetime now: %s, str now: %s' % (dt_now, str_now))
    dt_now = parse_iso8601(str_now)
    print('str now: %s, datetime now: %s' % (str_now, dt_now))
