from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/status')
def status():
    return jsonify({"status": "OK"})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({"error": "Missing 'a' or 'b'"}), 400
    return jsonify({"result": a * b})

