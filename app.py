from flask import Flask, request, jsonify
from database import init_db
import sqlite3
from calculator import calculate_payoff_month


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



@app.route("/debts", methods = ["GET"])
def get_debts():
    connection = sqlite3.connect("zeroday.db")
    cursor  = connection.cursor()
    cursor.execute("SELECT * FROM debts ORDER BY interest_rate DESC") 
    rows = cursor.fetchall()
    connection.close()

    debts = []
    for row in rows:
        debts.append({
            "id": row[0],
            "name": row[1],
            "balance": row[2],
            "interest_rate": row[3],
            "minimum_payment": row[4],
            "payoff_months": calculate_payoff_month(row[2], row[3], row[4])
        })
    
    return jsonify(debts)


@app.route("/debts/<int:id>", methods=["DELETE"])
def delete_debt(id):
    connection = sqlite3.connect("zeroday.db")
    cursor  = connection.cursor()
    cursor.execute("DELETE FROM debts WHERE id = ?", (id,))
    connection.commit()
    connection.close() 


    return jsonify({"message": "Debt deleted successfully"}), 200
 


    
    


if __name__ == "__main__":
    app.run(debug=True)