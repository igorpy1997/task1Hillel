from flask import Flask, redirect

from random import randint

app = Flask(__name__)

constant = [1, 2, 3]


@app.route("/")
def show_items():
    return f"<h3>Our Items are: {constant}!!!<h3>"


@app.route("/delete_item")
def delete_item():
    constant.pop()
    return redirect("/")


@app.route("/add_item")
def add_item():
    constant.append(randint(0, 100))
    return redirect("/")


if __name__ == "__main__":
    app.run(host="localhost", port=8000)
