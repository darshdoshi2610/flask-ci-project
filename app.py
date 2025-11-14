from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route("/status")
def status():
    return jsonify({"status": "ok"})

@app.route("/sum")
def sum_numbers():
    a = request.args.get("a")
    b = request.args.get("b")
    try:
        ai = float(a)
        bi = float(b)
    except:
        abort(400, "a and b must be numbers")

    result = ai + bi
    return jsonify({"sum": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
