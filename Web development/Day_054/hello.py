from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return ('<h1>Hello world</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmV1aGNpZ3c5aXJ0bWVtYWt3YTBycjdtZ2ZheXpsMHkxdjZzbGJmMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kfdazeFAkjHHQUBvXH/giphy-downsized-large.gif", width=200px>'
            )


#different routes using the app.route decorator
@app.route('/bye')
def say_bye():
    return "Bye"

# creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello hello {name}. You are {number} years old"

if __name__ == "__main__":
    # run the app in debug mode to auto-reload
    app.run(debug=True)
