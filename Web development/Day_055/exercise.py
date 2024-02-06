from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

def make_bigger(function):
    def wrapper():
        return "<h1>" + function() + "</h1>"
    return wrapper


@app.route('/')
def say_hello():
    return "hello"

@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
@make_bigger
def say_bye():
    return "bye"
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"hello there {name}! You are are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)