from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    pizzas = [
        {"name": "Пепероні", "ingredients": "Ковбаса, сир, перепорні", "price": 220},
        {"name": "Сирна", "ingredients": "Сир, соус", "price": 150},
        {"name": "Гавайська", "ingredients": "Курину м'ясо, сир, ананас, кукурудза", "price": 230}
    ]
    return render_template("menu.html", pizzas=pizzas)


if __name__ == "__main__":
    app.run(debug=True, port=80)