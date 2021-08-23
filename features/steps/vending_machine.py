from behave import *

@given(u'The vending machine is running')
def step_impl(context):
    context.browser.get(context.base_url)


@when(u'The "{button}" button is pushed')
def step_impl(context, button):
    context.browser.find_element_by_id(button).click()


@then(u'"{product}" will be dispensed')
def step_impl(context, product):
    expected = f'DISPENSING {product.upper()}...'
    actual = context.browser.find_element_by_id('dispenser').text
    
    assert actual == expected, f'Expected dispenser to have {expected}, but it is {actual}'


@then(u'The dislay will say "{message}"')
def step_impl(context, message):
    display = context.browser.find_element_by_id('display').text

    assert display == message, f'Expected display to show {message} but it shows {display}'
