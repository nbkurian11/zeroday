from flask import Flask, request, jsonify
from database import init_db
import sqlite3


app = Flask(__name__)
init_db()

@app.route("/")
def greeting():
    return "ZeroDay is running"


@app.route("/debts", methods = ["POST"])
def add_debt():
    data = request.get_json(force = True)
    name = data.get("name")
    balance = data.get("balance")
    interest_rate = data.get("interest_rate")
    minimum_payment = data.get("minimum_payment")

    connection = sqlite3.connect("zeroday.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO debts (name, balance, interest_rate, minimum_payment) VALUES (?, ?, ?, ?)",
    (name, balance, interest_rate, minimum_payment)
    )
    connection.commit()
    connection.close()

    return jsonify({"message": "Debt added successfully"}), 201



if __name__ == "__main__":
    app.run(debug=True)