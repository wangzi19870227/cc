def aaa(*args, **kwargs):
    print args
    print kwargs

aaa('aaa', 111, None, id='xxx', name='yyy')

args = ('aaa', 111, None)
kwargs = {'id': 'aaa',
          'name': 'bbb'}
aaa(*args, **kwargs)
