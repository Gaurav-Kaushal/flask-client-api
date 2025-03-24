import os
from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
#    app.config["MONGO_URI"] = "mongodb://flask_user:flaskpassword@localhost:27017/clients_db?authSource=clients_db"
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://flask_user:flaskpassword@localhost:27017/clients_db")
    mongo.init_app(app)

def get_db():
    return mongo.db if mongo.cx else None
