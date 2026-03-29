from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app) 

@app.route("/check", methods=["POST"])
def check_url():
    data = request.json
    url = data.get("url")

    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        end = time.time()

        return jsonify({
            "status": "UP" if response.status_code == 200 else "DOWN",
            "status_code": response.status_code,
            "response_time": round((end - start) * 1000, 2)
        })

    except Exception as e:
        return jsonify({
            "status": "DOWN",
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)