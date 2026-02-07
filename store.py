from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/about/<username>")
def about_page(username):
    return f"<h1>This is the about page of {username}</h1>"

@app.route("/market")
def market_page():
    items = [
        {'id': 1, 'name': 'Pikachu', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Charmander', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Lugia', 'barcode': '231985128446', 'price': 2000},
        {'id': 4, 'name': 'Mewtwo', 'barcode': '841965028223', 'price': 1200}
    ]
    return render_template("market.html", items=items)


