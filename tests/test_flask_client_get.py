import json
import requests
from urllib import urlencode


# method 1: do not specify encode method, will auto urlencode
# we can only use request.args(request.query_string) to get params.
# request.args can get a ImmutableMultiDict object, 
# request.query_string can get a urlencoded string.
url = 'http://127.0.0.1:50000/send_sms'
payload = {
    "tos": '13641167229, 13641167229',
    "content": "aaa",
}
print payload
r = requests.get(url, params=payload)
print r.text

# method 2: specify use urlencode
# we can only use request.args(request.query_string) to get params
# request.args can get a ImmutableMultiDict object, 
# request.query_string can get a urlencoded string.
url = 'http://127.0.0.1:50000/send_sms'
payload = {
    "tos": '13641167229, 13641167229',
    "content": "aaa",
}
payload = urlencode(payload)
print payload
r = requests.get(url, params=payload)
print r.text

# Notice: do not specify use json encode, or server will parse failed!
