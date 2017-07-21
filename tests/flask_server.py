#https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832704232d6fb5df42dd34a7890fa6254351faac7000

import urlparse
from flask import Flask, request, redirect, url_for
from jsonschema import validate

app = Flask(__name__)


def validate_request(schema):
    params = None
    if request.method == 'POST':
        # for json encode
        try:
            # notice: this params must have, or will get failed!
            params = request.get_json(force=True, silent=True)
        except:
            pass

        # for url encode
        if params is None:
            qs = request.get_data()
            params = urlparse.parse_qs(qs, keep_blank_values=True)
            for key in params.keys():
                params[key] = params[key][0]
    else:
        # for url encode only
        params = request.args

    validate(params, schema)

    return params


def debug_request():
    #print "dir(request): %s" % dir(request)
    #print "endpoint: %s" % request.endpoint
    #print "environ: %s" % request.environ
    #print "headers: %s" % request.headers
    #print "values: %s" % request.values
    print "request.url: %s" % request.url
    print "request.method: %s" % request.method 
    # fetch GET params string
    print "request.args: %s, type: %s" % (request.args, type(request.args)) 
    print "request.query_string: %s, type: %s" % (request.query_string, type(request.query_string))
    ## fetch POST data, return a json/url encode string
    #print "request.data: %s, type: %s" % (request.data, type(request.data))
    # fetch POST data, return a json/url encode string
    print "request.get_data(): %s, type: %s" % (request.get_data(), type(request.get_data()))
    # fetch POST data with json encode, return a dict object
    get_json_true_true = request.get_json(force=True, silent=True)
    get_json_true_false = request.get_json(force=True, silent=False)
    get_json_false_true = request.get_json(force=False, silent=True)
    get_json_false_false = request.get_json(force=False, silent=False)
    print "request.get_json(): %s" % request.get_json()
    print "request.get_json(force=True, silent=True): %s, type: %s" % (get_json_true_true, type(get_json_true_true))
    print "request.get_json(force=True, silent=False): %s, type: %s" % (get_json_true_false, type(get_json_true_false))
    print "request.get_json(force=False, silent=True): %s, type: %s" % (get_json_false_true, type(get_json_false_true))
    print "request.get_json(force=False, silent=False): %s, type: %s" % (get_json_false_false, type(get_json_false_false))


@app.route('/index')
def index():
    return redirect(url_for('env'))


@app.route('/env')
def env():
    return 'v0.1'


@app.route('/user/<username>', methods=['GET'])
def get_user_info(username):
    print 'get_user_info() username: %s' % username
    print 'get_user_info() ok.'
    return 'username'


@app.route('/send_sms', methods=['GET', 'POST'])
def send_sms():
    debug_request()
    params = validate_request({
        'type': 'object',
        'properties': {
            'tos': {'type': 'string'},
            'content': {'type': 'string'},
        },
        'required': ['tos', 'content']
    })
    tos = params['tos']
    content = params['content']
    print 'send_sms() tos: %s, content: %s' % (tos, content)

    if request.method == 'POST':
        print 'send_sms() post ok.'
    else:
        print 'send_sms() get ok.'

    return 'msg_id hahah'


@app.route('/', methods=['POST'])
def call():
    params = validate_request({
        'type': 'object',
        'properties': {
            'action': {'type': 'string'},
        },
        'required': ['action']
    })
    action = params['action']
    return do_action(action)


def do_action(action):
    switch = {
        'CreateProject': create_project,
    }
    if action in switch:
        return switch[action]()
    else:
        raise Exception('Unknown action %s.' % action, 4000)


def create_project():
    print 'create project.'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50000, debug=True)
