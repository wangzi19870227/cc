# coding: utf-8

import json
import requests
from urllib import urlencode

# method 1: json encode
# we can use request.get_json(force=True, ...),
# and request.get_data() to get params.
# request.get_json(...) can get a Dict object, 
# request.get_data() can get a json encoded string.
# Notice: json encode params support dict/list, here use dict for example.
url = 'http://127.0.0.1:50000/send_sms'
payload = {
    "tos": '13641167229, 13641167229',
    #"content": "aaa",
    "content": "啊啊啊",
}
payload = json.dumps(payload) 
print payload
r = requests.post(url, data=payload)
#print r
print r.text


# method 2: urlencode
# we can only use request.get_data() to get params.
# request.get_data() can get a json encoded string.
# Notice: urlencode params only support dict!
url = 'http://127.0.0.1:50000/send_sms'
payload = {
    "tos": '13641167229, 13641167229',
    "content": "aaa",
}
payload = urlencode(payload)
print payload
r = requests.post(url, data=payload)
print r.text
