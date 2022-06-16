from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        text = function()
        return f'<b>{text}</b>'
    return wrapper_function


def make_italics(function):
    def wrapper_function():
        text = function()
        return f'<em>{text}</em>'
    return wrapper_function

def make_italics(function):
    def wrapper_function():
        text = function()
        return f'<em>{text}</em>'
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        text = function()
        return f'<u>{text}</u>'
    return wrapper_function

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@make_bold
@make_italics
@make_underline
def bye():
    return 'Bye!'

@app.route('/<name>')
def greet(name):
    return f"<h1>Hello there {name} <h1>" \
           f"<p>Live in peace! </p>" \
           f"<img src='https://cdn5.vectorstock.com/i/1000x1000/86/64/om-and-mandala-vector-15418664.jpg'>"


if __name__ =='__main__':
    app.run(debug=True)