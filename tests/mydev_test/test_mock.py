from mock import patch

def get_falcon_query_url():
    return config.CONF.falcon_query_url + '/graph/history'

def call():
    return [{'name': 'aaa', 'id': 'bbb'}]

def query_history():
    url = get_falcon_query_url()
    print url
    ret = call()
    print ret

def mock_get_falcon_query_url():
    return 'aaa'

def mock_call():
    return 'bbb'

with patch('__main__.get_falcon_query_url') as mock:
    mock.return_value = 'aaa'
    with patch('__main__.call') as mock:
        mock.return_value = 'bbb'
        query_history()

with patch('__main__.get_falcon_query_url', return_value='aaa'):
    with patch('__main__.call', return_value='bbb'):
        query_history()

with patch('__main__.get_falcon_query_url', 
           return_value=mock_get_falcon_query_url()):
    with patch('__main__.call', return_value=mock_call()):
        query_history()

@patch('__main__.get_falcon_query_url', mock_get_falcon_query_url)
@patch('__main__.call', mock_call)
def query_history_v2():
    url = get_falcon_query_url()
    print url
    ret = call()
    print ret
query_history_v2()

