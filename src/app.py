from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def vend():
    return render_template('index.html')
