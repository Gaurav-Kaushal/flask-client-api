from flask import Blueprint, request, jsonify, current_app
from app.models import Client
from app.db import get_db

api_bp = Blueprint("api", __name__)

@api_bp.route("/", methods=["GET"])
def home():
    return "Flask API is running!"

@api_bp.route("/clients", methods=["GET"])
def get_clients():
    db = get_db()  
    collection = db.clients
    clients = list(collection.find({}, {"_id": 0}))
    return jsonify(clients)

@api_bp.route("/clients", methods=["POST"])
def add_client():
    db = get_db()  
    collection = db.clients

    if not request.is_json:
        return jsonify({"error": "Request must be in JSON format"}), 415

    data = request.get_json()

    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Missing required fields"}), 400

    collection.insert_one(data)
    return jsonify({"message": "Client added successfully"}), 201


@api_bp.route("/clients/<email>", methods=["GET"])
def get_client(email):
    db = get_db()  
    collection = db.clients
    client = collection.find_one({"email": email}, {"_id": 0})
    if not client:
        return jsonify({"error": "Client not found"}), 404
    return jsonify(client)

@api_bp.route("/clients/<email>", methods=["PUT"])
def update_client(email):
    db = get_db()  
    collection = db.clients
    data = request.json
    updated = collection.update_one({"email": email}, {"$set": data})
    if updated.matched_count == 0:
        return jsonify({"error": "Client not found"}), 404
    return jsonify({"message": "Client updated successfully"})

@api_bp.route("/clients/<email>", methods=["DELETE"])
def delete_client(email):
    db = get_db()  
    collection = db.clients
    deleted = collection.delete_one({"email": email})
    if deleted.deleted_count == 0:
        return jsonify({"error": "Client not found"}), 404
    return jsonify({"message": "Client deleted successfully"})
