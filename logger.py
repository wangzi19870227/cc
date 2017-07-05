import logging
from logging.handlers import TimedRotatingFileHandler


# default log_file is None, will get a StreamHandler, with debug level.
# if log_file specified, then get a TimedRotatingFileHandler, when specified level.
def get_logger(name, log_file=None, log_level=logging.INFO,
               rotating_when='D', rotating_interval=7, backup_count=30):
    logger = logging.getLogger(name)

    # if exist, get this already exist one
    if logger.handlers:
        return logger

    # if not exist, then get a new one
    if log_file:
        logger.setLevel(log_level)
        handler = TimedRotatingFileHandler(
            log_file,
            when=rotating_when,
            interval=rotating_interval,
            backupCount=backup_count)
    else:
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] [%(name)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


if __name__ == '__main__':

    def test_stream_handler():
        LOG = get_logger(__file__)
        LOG1 = get_logger(__file__)
        LOG2 = get_logger('aa')
        print LOG
        print LOG1
        print LOG2
        LOG.debug('debug')
        LOG.info('info')
        LOG.warn('warn')
        LOG.error('error')
        LOG.critical('critical')

    def test_timed_rotating_file_handler():
        import os
        import time

        def mk_dir(path):
            if not os.path.exists(path):
                os.makedirs(path)

        app_name = 'aaa'
        log_path = os.path.join('/var/log/', app_name)
        mk_dir(log_path)
        log_file = os.path.join(log_path, app_name + '.log')
        LOG = get_logger(__file__, log_file=log_file, rotating_when='S',
                         rotating_interval=2, backup_count=3)
        while True:
            LOG.debug('debug')
            LOG.info('info')
            LOG.warn('warn')
            LOG.error('error')
            LOG.critical('critical')
            time.sleep(1)

    def test_root_logger():
        logging.basicConfig(
            level=logging.DEBUG,
            format='[%(levelname)s] [%(asctime)s] [%(name)s] %(message)s')
        logging.debug('debug')
        logging.info('info')
        logging.warn('warn')
        logging.error('error')
        logging.critical('critical')
        

    #test_stream_handler()
    #test_timed_rotating_file_handler()
    test_root_logger()
