import os
from flask import Flask, jsonify

# Экземпляр Flask
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello from Secure CI/CD Pipeline!")

@app.route('/health')
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    # Берём значения из переменных окружения
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "0") == "1"

    app.run(host=host, port=port, debug=debug)

