from behave import *


@given("I search for a valid book")
def sample_test(context):
    print("I search for a valid book")


@given(u'I search for a invalid book')
def step_impl(context):
    print("I search for a invalid book")


@then('the result page will include "{text}"')
def step_impl(context, text):
    print(f"{text}")
