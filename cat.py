import random 
from flask import Flask,render_template
app = Flask(__name__)
x = ["orel","urewka"]
@app.route("/")
def main_page():
    return render_template("index.html")
# @app.route("loi")
# def main_page():
#     return "<h1>не разбрасывай свои вещи)</h1><a href='blog'>привет</a>"

# @app.route("/home")
# def monetka():
#     return f'{random.choice(x)}'
# @app.route("/yui")
# def monetka():
#     return f'{random.choice(x)}'
@app.route("/game")
def game_page():
    return render_template("game.html")
@app.route("/kartunku")
def kartunku_page():
    return render_template("kartunku.html")
@app.route("/kocmo")
def kocmo_page():
    return render_template("kocmo.html")

app.run(debug=True)