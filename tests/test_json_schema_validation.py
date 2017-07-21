# http://json-schema.org/latest/json-schema-validation.html
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def assert_validate_success(param, schema):
    try:
        validate(param, schema) # success
    except ValidationError:
        raise

def assert_validate_failed(param, schema):
    try:
        validate(param, schema) # error
    except ValidationError:
        pass

# test integer
schema = {'type': 'integer',
          'minimum': 0,
          'maxinum': 10}
assert_validate_failed('1', schema)
assert_validate_failed(None, schema)
assert_validate_failed(True, schema)
assert_validate_failed([1], schema)
assert_validate_failed(0.1, schema)
assert_validate_failed(-1, schema)
assert_validate_success(1, schema)
assert_validate_success(0, schema)

# test number
schema = {'type': 'number',
          'minimum': 0,
          'maxinum': 10}
assert_validate_failed('1', schema)
assert_validate_failed(None, schema)
assert_validate_failed(True, schema)
assert_validate_failed([1], schema)
assert_validate_failed(-1, schema)
assert_validate_success(0.1, schema)
assert_validate_success(1, schema)
assert_validate_success(0, schema)

# test string
schema = {'type': 'string',
          'minLength': 1,
          'maxLength': 10}
assert_validate_failed(1, schema)
assert_validate_failed(None, schema)
assert_validate_failed(True, schema)
assert_validate_failed([1], schema)
assert_validate_failed('1'*20, schema)
assert_validate_success('1', schema)

# test boolean
schema = {'type': 'boolean',
          'minLength': 1,
          'maxLength': 10}
assert_validate_failed(1, schema)
assert_validate_failed(None, schema)
assert_validate_success(True, schema)

# test array
schema = {'type': 'array',
          'items': {'type': 'string'},
          'minItems': 1,
          'maxItems': 3,
          'uniqueItems': True}
assert_validate_failed('1', schema)
assert_validate_failed(None, schema)
assert_validate_failed(True, schema)
assert_validate_failed([], schema)
assert_validate_failed(['1', '2', '3', '4'], schema)
assert_validate_success(['1'], schema)

# test object
schema = {'type': 'object',
          'properties': {
              'id': {'type': 'string'},
              'name': {'type': 'string'}
          },
          'required': ['id']
          }
assert_validate_success({'id': '1'}, schema)
assert_validate_failed({'name': 'xxx'}, schema)
assert_validate_success({'id': '1', 'name': 'xxx'}, schema)

schema = {'type': 'object',
          'properties': {
              'id': {'type': 'string'},
              'quotaSet': {
                  'type': 'array',
                  'items': {
                      'type': 'object',
                      'properties': {
                          'qtServers': {'type': 'integer'},
                          'cuServers': {'type': 'integer'},
                      },
                      'required': ['qtServers']
                   },
                  'minItems': 0,
                  'maxItems': 10,
                  'uniqueItems': False
              }
          },
          'required': ['id']
          }
assert_validate_success({'id': '1'}, schema)
assert_validate_failed({'id': '1', 'quotaSet': []}, schema)
assert_validate_success({'id': '1', 'quotaSet': [{'qtServers': 1}]}, schema)
assert_validate_failed({'id': '1', 'quotaSet': [{'cuServers': 1}]}, schema)
assert_validate_success({'id': '1', 'quotaSet': [{'qtServers': 1}]}, schema)
assert_validate_failed({'id': '1', 'quotaSet': [{'qtServers': 1, 'cuServers':
    1}]}, schema)

