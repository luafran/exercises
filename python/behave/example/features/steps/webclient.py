import requests
import unittest

@given(u'service is running')
def step(context):
   pass 

@when(u'I use a valid latitude')
def step(context):
    context.query['latitude'] = '45.534251'

@when(u'I use a valid longitude')
def step(context):
    context.query['longitude'] = '-122.6754'

@when(u'i do not use latitude')
def step(context):
    pass

@when(u'i do not use longitude')
def step(context):
    pass

@when(u'I use an invalid latitude')
def step(context):
    context.query['latitude'] = '91'

@when(u'I use an invalid longitude')
def step(context):
    context.query['longitude'] = '-181'

@when(u'I do a poi request')
def step(context):
    context.response = requests.get('http://Choices-TEST-1275948226.us-east-1.elb.amazonaws.com/context/choices/v1/pois', params=context.query)
    print context.response.url

@then(u'service returns Bad Request')
def step(context):
    #unittest.TestCase.assertEqual(unittest.TestCase(), 500, context.response.status_code)
    assert context.response.status_code == 400

@then(u'service returns Ok')
def step(context):
    #unittest.TestCase.assertEqual(unittest.TestCase(), 500, context.response.status_code)
    assert context.response.status_code == 200

