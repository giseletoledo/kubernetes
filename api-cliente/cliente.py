from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def usar_calculadora():
    try:
        r = requests.get("http://api-calculadora-service:8080/calc")
        return jsonify({"resultado": r.json()})
    except:
        return jsonify({"erro": "Não foi possível acessar a calculadora"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
