from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/calc")
def calcular():
    a, b = 10, 5
    resultado = {
        "soma": a + b,
        "subtracao": a - b,
        "multiplicacao": a * b,
        "divisao": a / b,
    }
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

