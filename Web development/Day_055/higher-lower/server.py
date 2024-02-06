from flask import Flask
app = Flask(__name__)
from random import choice

number = 4 #choice(list(range(0, 9)))
print(number)
@app.route("/")
def get_number():
    return ("<h1>Guess the number from 0 to 9</h1>"
            "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>")

@app.route("/<int:num>")
def check_number(num):
    if num == number:
        return ("<h1 style='color: green'>You got it!</h1>"
            "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>")
    elif num < number:
        return ("<h1 style='color: red'>Too low</h1>"
            "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>")
    else:
        return ("<h1 style='color: purple'>Too high</h1>"
            "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>")


if __name__ == "__main__":
    app.run(debug=True)