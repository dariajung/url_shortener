from flask import (Flask, Response, request, render_template)
import shorten
import redis

app = Flask(__name__)

app.debug = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def return_shortened():
    url_to_parse = request.form.get('url_to_parse')
    print url_to_parse

    return "OK"


if __name__ == '__main__':
    app.run()