from behave import *
import requests
from config.test_run_config import *
use_step_matcher("re")

@Given('user is logged in youtrack')
def step_impl(context):
    pass

@step('json response is retrieved with list of projects')
def step_impl(context):
    context.response = context.s.get(URL)
    # print("list of projects =", context.response.json())

@then('verify that status code returned is 200')
def step_impl(context):
    # print ("Status code =",context.response.status_code)
    assert context.response.status_code == 201, "Response code is different: %s" % context.response.status_code + \
                                               "   Error: " + str(context.response.content)

@step('user should be able to add an issue to 0-1')
def step_impl(context):
    endpoint = 'https://apitesting.myjetbrains.com/youtrack/api/issues'
    json ={
                  # "project": {"id": project_id},
                  "project": {"id": "0-1"},
                  "summary": "Created one more issue using Docker image by maintaining session object!",
                  "description": "Created  one more issue using Docker image by maintaining session object."
          }
    resp = context.s.post(endpoint, json=json)
    resp_json = resp.json()
    # print("created issue json =", resp_json)
