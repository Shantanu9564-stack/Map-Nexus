from flask import Flask, jsonify, render_template
import requests
import time

app = Flask(__name__)

cached_data = {"states": []}
last_fetch = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/flights")
def flights():
    global cached_data, last_fetch

    now = time.time()

    # ⏱ cache for 5 seconds
    if now - last_fetch > 5:
        try:
            res = requests.get("https://opensky-network.org/api/states/all", timeout=10)
            cached_data = res.json()
            last_fetch = now
        except:
            pass

    return jsonify(cached_data)

if __name__ == "__main__":
    app.run(debug=True)
