# Flask Clients API

This is a simple Flask API for managing clients with MongoDB.

##  Features

- CRUD operations for clients
- MongoDB integration
- Unit tests with pytest
- Dockerized for easy deployment

## Setup Instructions

### 1️⃣ Install Dependencies

```sh
pip install -r requirements.txt

```

### 2️⃣ Set Up Environment Variables

Create a `.env` file:

```sh
MONGO_URI=mongodb://localhost:27017/

```

### 3️⃣ Run the Flask App

```sh
python main.py

```

### 4️⃣ Run Tests

```sh
pytest tests/

```

### 5️⃣ Run with Docker

```sh
docker build -t flask-clients-api .
docker run -p 5000:5000 flask-clients-api

```
