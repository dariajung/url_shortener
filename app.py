from flask import Flask
from flask import render_template
import shorten

app = Flask(__name__)

app.debug = True

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()