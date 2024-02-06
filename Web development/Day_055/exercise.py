from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def inner_func():
        function()
    return inner_func()


@app.route('/')
def say_hello():
    return "hello"

@app.route('/bye')
@make_bold
def say_bye():
    return "bye"
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"hello there {name}! You are are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)