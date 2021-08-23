from flask import Flask, request
from flask.templating import render_template
from src.machine import Machine

app = Flask(__name__)
machine = Machine()

coin_slot = {
    'PENNY': {'weight': 2.5, 'diameter': .75, 'thickness': 1.52},
    'NICKEL': {'weight': 5.0, 'diameter': .835, 'thickness': 1.95},
    'DIME': {'weight': 2.268, 'diameter': .705, 'thickness': 1.35},
    'QUARTER': {'weight': 5.670, 'diameter': .955, 'thickness': 1.75}
}

@app.route('/', methods=['GET'])
def get_vending_machine():
    machine.__init__()
    return _render()


@app.route('/', methods=['POST'])
def post_vending_machine():
    if request.form.get('product_button'):
        product = request.form.get('product_button')
        machine.dispense(product)

    if request.form.get('coin_button'):
        dimensions = coin_slot[request.form.get('coin_button')]
        machine.add_coin(dimensions['weight'], dimensions['diameter'], dimensions['thickness'])

    return _render()


def _render():
    coin_return = format(machine.coin_return_in_cents / 100, '.2f')
    amount_entered = 'INSERT COIN' if machine.amount_in_cents == 0 else format(machine.amount_in_cents / 100, '.2f')
    return render_template('index.html', dispenser=machine.dispenser, display=machine.display, amount_entered=amount_entered, coin_return=coin_return)
