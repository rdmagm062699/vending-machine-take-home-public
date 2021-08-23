from flask import Flask, request
from flask.templating import render_template
from src.machine import Machine

app = Flask(__name__)
machine = Machine()

coin_slot = {
    'PENNY': {'weight': 2.5, 'diameter': .75, 'thickness': 1.52}
}

@app.route('/', methods=['GET'])
def get_vending_machine():
    machine = Machine()
    coin_return = format(machine.coin_return_in_cents / 100, '.2f')
    return render_template('index.html', dispenser=machine.dispenser, display=machine.display, amount_entered='INSERT COIN', coin_return=coin_return)


@app.route('/', methods=['POST'])
def post_vending_machine():
    if request.form.get('product_button'):
        product = request.form.get('product_button')
        machine.dispense(product)

    if request.form.get('coin_button'):
        dimensions = coin_slot[request.form.get('coin_button')]
        machine.add_coin(dimensions['weight'], dimensions['diameter'], dimensions['thickness'])

    coin_return = format(machine.coin_return_in_cents / 100, '.2f')
    return render_template('index.html', dispenser=machine.dispenser, display=machine.display, amount_entered='INSERT COIN', coin_return=coin_return)
