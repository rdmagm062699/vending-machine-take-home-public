from flask import Flask, request
from flask.templating import render_template
from src.machine import Machine

app = Flask(__name__)
machine = Machine()


@app.route('/', methods=['GET'])
def get_vending_machine():
    machine = Machine()
    return render_template('index.html', dispenser=machine.dispenser, display=machine.display, amount_entered='INSERT COIN')


@app.route('/', methods=['POST'])
def post_vending_machine():
    product = request.form.get('product_button')
    machine.dispense(product)

    return render_template('index.html', dispenser=machine.dispenser, display=machine.display, amount_entered='INSERT COIN')
