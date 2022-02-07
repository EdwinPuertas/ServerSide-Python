from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hola Mundo'


@app.route('/home')
def home():
    return render_template('home.html', title="Home", content="Hello, World!")


if __name__ == '__main__':
    app.run()