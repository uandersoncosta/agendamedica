from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/appointments")
def appointments():
    return jsonify([
        {
            "patient": "João Silva",
            "cpf": "11111111111",
            "doctor": "Dr Carlos",
            "specialty": "Cardiologia",
            "date": "2026-07-25",
            "time": "09:00",
            "insurance": "Unimed",
            "status": "Confirmado"
        }
    ])


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )