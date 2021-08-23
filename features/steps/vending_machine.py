from behave import *

@given(u'The vending machine is running')
def step_impl(context):
    context.browser.get(context.base_url)


@when(u'The "{button}" button is pushed {pushes} time(s)')
def step_impl(context, button, pushes):
    for x in range(int(pushes)):
        context.browser.find_element_by_id(button).click()


@then(u'"{product}" will be dispensed')
def step_impl(context, product):
    expected = f'DISPENSING {product.upper()}...'
    actual = context.browser.find_element_by_id('dispenser').text
    
    assert actual == expected, f'Expected dispenser to have {expected}, but it is {actual}'


@then(u'nothing will be dispensed')
def step_impl(context):
    expected = ''
    actual = context.browser.find_element_by_id('dispenser').text
    
    assert actual == expected, f'Expected to not dispense anything'


@then(u'The display will say "{message}"')
def step_impl(context, message):
    display = context.browser.find_element_by_id('display').text

    assert display == message, f'Expected display to show {message} but it shows {display}'


@then(u'the amount entered will show "{message}"')
def step_impl(context, message):
    amount_entered = context.browser.find_element_by_id('amount_entered').text

    assert amount_entered == message, f'Expected amount entered to show {message} but it shows {amount_entered}'


@when(u'A "{coin}" is inserted')
def step_impl(context, coin):
    context.browser.find_element_by_id(coin).click()


@then(u'the coin return will have {amount}')
def step_impl(context, amount):
    coin_return = context.browser.find_element_by_id('coin_return').text

    assert float(amount) == float(coin_return)