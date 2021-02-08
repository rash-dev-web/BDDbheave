from behave import *
import requests


@given(u'request url and post body')
def step_impl(context):
    context.URL = "https://reqres.in/api/users"
    context.param = {
        "name": "morpheus",
        "job": "leader",
    }


# @when(u'send the url and json body')
# def step_impl(context):
#     context.response = requests.post(context.URL, data=context.param)


@when(u'send the url and json body with "{name}" and "{job}"')
def post_body(context, name, job):
    param1 = {
        "name": name,
        "job": job,
    }
    context.response = requests.post(context.URL, data=param1)


@then(u'Then Receive the Json response and status code as 201')
def step_impl(context):
    assert context.response.status_code == 201
    print(context.response.json())
