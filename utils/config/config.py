import os

CONF = None


def setup(gevent=False):
    class Config(object):
        def __init__(self):
            self.debug = os.getenv('DEBUG') or 'True'
            self.gevent = gevent
            self.manage_port = int(os.getenv('MANAGE_PORT') or 9004)

            # db
            self.db_host = os.getenv('DB_HOST') or None
            self.db_port = int(os.getenv('DB_PORT') or 3306)
            self.db_user = os.getenv('DB_USER') or None
            self.db_password = os.getenv('DB_PASSWORD') or None
            self.db_database = os.getenv('DB_DATABASE') or None

            # auth
            self.manage_key = os.getenv('MANAGE_KEY') or 'key'
            self.manage_secret = os.getenv('MANAGE_SECRET') or 'secret'

            # region
            self.region_id = os.getenv('REGION_ID') or 'test_region'

            # log
            self.app_root = os.path.dirname(os.path.abspath(__file__)).split('/')[-1]
            self.log_dir = os.getenv('LOG_DIR') or os.path.join('/var/log',
                    self.app_root)

            # notify
            self.slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL') or None
            self.notify_sms_url = os.getenv('NOTIFY_SMS_URL') or None
            self.notify_sms_key = os.getenv('NOTIFY_SMS_KEY') or None
            self.notify_sms_secret = os.getenv('NOTIFY_SMS_SECRET') or None
            self.notify_sms_mobiles = os.getenv('NOTIFY_SMS_MOBILE') or None
            self.app_name = self.region_id + '-' + self.app_root

    global CONF
    CONF = Config()


if __name__ == '__main__':
    setup()
    print('region_id: %s' % CONF.region_id)
    print('app_name: %s' % CONF.app_name)
    print('app_root: %s' % CONF.app_root)
