
from logging.handlers import TimedRotatingFileHandler

FILE_NAME='aaa.log'
FILE_MAX_SIZE=10*1024*1024
TR_WHEN='S' # S, M, H, D, W
TR_INTERVAL=10
BACKUP_COUNT=5

#handler = logging.StreamHandler()
#handler = RotatingFileHandler(
#    FILE_NAME,
#    maxBytes=FILE_MAX_SIZE,
#    backupCount=BACKUP_COUNT)
handler = TimedRotatingFileHandler(
    FILE_NAME,
    when=TR_WHEN,
    interval=TR_INTERVAL,
    backupCount=BACKUP_COUNT)
formatter = logging.Formatter('[%(levelname)s][%(asctime)s][%(name)s] %(message)s')
handler.setFormatter(formatter)

def get_logger():
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    import time

    logger = get_logger()
    while True:
        logger.debug('debug')
        logger.info('info')
        logger.warn('warn')
        logger.error('error')
        logger.critical('critical')
        logger.trace = logger.critical
        logger.trace('trace')
        time.sleep(1)
