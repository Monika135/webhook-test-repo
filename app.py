

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def start():
    return "Hello There!!"


@app.route("/form/data", methods=["POST"])
def get_data():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    print(name, email, phone)

    return jsonify({"status": "received"}), 200


if __name__ == "__main__":
    app.run(port=5001, debug=True)
