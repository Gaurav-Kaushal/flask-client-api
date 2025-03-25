from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from app import create_app

#app = Flask(__name__)
app = create_app()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client.clients_db
collection = db.clients

@app.route("/clients", methods=["GET"])
def get_clients():
    clients = list(collection.find({}, {"_id": 0}))
    return jsonify(clients)

@app.route("/clients", methods=["POST"])
def add_client():
    data = request.json
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Missing required fields"}), 400
    collection.insert_one(data)
    return jsonify({"message": "Client added successfully"}), 201

@app.route("/clients/<email>", methods=["GET"])
def get_client(email):
    client = collection.find_one({"email": email}, {"_id": 0})
    if not client:
        return jsonify({"error": "Client not found"}), 404
    return jsonify(client)

@app.route("/clients/<email>", methods=["PUT"])
def update_client(email):
    data = request.json
    updated = collection.update_one({"email": email}, {"$set": data})
    if updated.matched_count == 0:
        return jsonify({"error": "Client not found"}), 404
    return jsonify({"message": "Client updated successfully"})

@app.route("/clients/<email>", methods=["DELETE"])
def delete_client(email):
    deleted = collection.delete_one({"email": email})
    if deleted.deleted_count == 0:
        return jsonify({"error": "Client not found"}), 404
    return jsonify({"message": "Client deleted successfully"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
