import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://flask_user:secure@localhost:27017/clients_db?authSource=clients_db")
