

# # @app.route("/webhook", methods=["POST"])
# # def payment_webhook():
# #     payload = request.get_json(force=True)

# #     if not payload:
# #         abort(400, "Invalid JSON")

# #     try:
# #         validate_payload(payload)
# #     except ValueError as ve:
# #         return jsonify({"error": str(ve)}), 400

# #     # Add timestamp
# #     payload["received_at"] = datetime.utcnow().isoformat()

# #     log_event(payload)
# #     print(
# #         f"✅ Received: {payload['event_type']} | ID: "
# #         f"{payload.get('transaction_id')}")

# #     return jsonify({"status": "received"}), 200


# if __name__ == "__main__":
#     app.run(port=5002, debug=True)


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
