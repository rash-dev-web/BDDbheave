from behave import *


@given('a set of specific users')
def step_impl(context):
    for row in context.table:
        print(f"Name: {row['name']}")
        print(f"Department: {row['department']}")


@when(u'we count the number of people in each department')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When we count the number of people in each department')


@then(u'we will find two people in "Silly Walks"')
def step_impl(context):
    pass


@then(u'we will find one person in "Beer Cans"')
def step_impl(context):
    pass
