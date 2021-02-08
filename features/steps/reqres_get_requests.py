from behave import *
import requests


@given("the request url and parameter")
def setup(context):
    context.param = {
        "page": 2,
    }
    context.URL = "https://reqres.in/api/users"


@when("submit the list user request")
def list_users(context):
    context.response = requests.get(context.URL, params=context.param)
    print(context.response.json())


@then("get the response as number of users and status code as 200")
def validate_users_response(context):
    assert context.response.status_code == 200
