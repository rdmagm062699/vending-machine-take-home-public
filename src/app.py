from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_vending_machine():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def post_vending_machine():
    dispenser = 'DISPENSING COLA...'
    display = 'THANK YOU'

    return render_template('index.html', dispenser=dispenser, display=display)
