# Flask Clients API Documentation

## Overview
This **Flask API** provides CRUD (Create, Read, Update, Delete) operations for managing clients, with data stored in **MongoDB**. It supports **Dockerization**, **Kubernetes deployment**, and **CI/CD pipeline integration** along with proper health checks.

## Features
- Connects to **MongoDB**
- Handles **CRUD operations** (`GET`, `POST`, `PUT`, `DELETE`)
- Supports **Docker & Kubernetes**
- Includes **health check** endpoint
- Works with **Postman** and **curl**
- Integrated with **CI/CD pipelines**
- Secured using **Let's Encrypt TLS Certificate**
- Auto-scales using **Horizontal Pod Autoscaler (HPA)**
- Exposed via **Ingress Controller & Load Balancer**

---
##  Project Structure
```
flask-clients-api/
│── app/
│   ├── __init__.py          
│   ├── routes.py            
│   ├── models.py           
│   ├── config.py            
│   ├── db.py                
│── tests/
│   ├── test_api.py          
│── k8s/                     
│   ├── deployments/
│   ├── ingress/
│   ├── services/
│   ├── secrets/
│   ├── hpa/
│── Dockerfile    
│── .github/workflows/
│── requirements.txt         
│── .env                     
│── .gitignore              
│── README.md                
│── main.py                  
```

---
## API Endpoints

### Health Check
**Request:**
```http
GET /health
```
**Response:**
```json
{"status": "ok"}
```

### Get All Clients
**Request:**
```http
GET /clients
```
**Response:**
```json
[
    { "name": "John Doe", "email": "john@example.com" }
]
```

### Add a New Client
**Request:**
```http
POST /clients
```
**Headers:**
```json
Content-Type: application/json
```
**Body:**
```json
{
    "name": "Alice",
    "email": "alice@example.com"
}
```
**Response:**
```json
{"message": "Client added successfully"}
```

### Get a Specific Client by Email
**Request:**
```http
GET /clients/alice@example.com
```
**Response:**
```json
{ "name": "Alice", "email": "alice@example.com" }
```

### Update a Client’s Details
**Request:**
```http
PUT /clients/alice@example.com
```
**Headers:**
```json
Content-Type: application/json
```
**Body:**
```json
{ "name": "Alice Smith" }
```
**Response:**
```json
{"message": "Client updated successfully"}
```

### Delete a Client
**Request:**
```http
DELETE /clients/alice@example.com
```
**Response:**
```json
{"message": "Client deleted successfully"}
```

---
## Setup and Running Locally

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file:
```env
MONGO_URI=mongodb://flask_user:flaskpassword@localhost:27017/clients_db?authSource=clients_db
```

### Run the Flask App
```sh
python main.py
```

### Test with Postman or curl
```sh
curl http://127.0.0.1:5000/clients
```

---
## Running with Docker
### Build Docker Image
```sh
docker build -t flask-clients-api .
```

### Run Docker Container
```sh
docker run -p 5000:5000 flask-clients-api
```

---
## Deployment to Kubernetes
This API is deployed using Kubernetes with the following components:
- Load Balancer (Exposes the service)
- Ingress Controller (Routes traffic)
- Horizontal Pod Autoscaler (HPA) (Auto-scales API pods)
- Let's Encrypt Certificate Manager (TLS/SSL for HTTPS)

### Apply All Kubernetes Manifests (First-time Deployment)
```sh
kubectl apply -f k8s/
```

### Check Deployment Status
```sh
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get ingress
```

### Horizontal Pod Autoscaler (HPA)
```sh
kubectl apply -f k8s/hpa/
kubectl get hpa
```

---
## CI/CD Pipeline
The project includes a GitHub Actions workflow that:
- Builds and tests the application
- Builds and pushes the Docker image
- Deploys only changed Kubernetes manifests

If deploying for the first time, manually apply the Kubernetes manifests:
```sh
kubectl apply -f k8s/
```

For future updates, CI/CD will apply changes automatically.

---
## Update DuckDNS IP Manually
Since we are using DuckDNS, the public IP of the Load Balancer must be manually updated.

Find the Load Balancer IP:
```sh
nslookup <load-balancer-hostname>
```

Use the output IP to update DuckDNS:
```sh
echo "<IP_ADDRESS>" > ~/.duckdns/gkeks.duckdns.org
```

## Troubleshooting

### MongoDB connection error
Ensure MongoDB is running:
```sh
mongosh
use clients_db
show collections
```

### API not responding
Check logs:
```sh
kubectl logs -f deployment/flask-api
```

### Horizontal Pod Autoscaler not working
Ensure Metrics Server is available:
```sh
kubectl get apiservice v1beta1.metrics.k8s.io
kubectl top pods
```
If missing endpoints, patch the Metrics Server:
```sh
kubectl patch svc -n kube-system metrics-server --type='json' -p '[{"op": "replace", "path": "/spec/ports/0/targetPort", "value": 10251}]'
kubectl rollout restart deployment metrics-server -n kube-system
```

---
## Notes
- The original domain `clients.api.deltacapita.com` has been replaced with `gkeks.duckdns.org`.
- Certificate has been issued successfully using Let's Encrypt.
- The project is deployed with **Kubernetes LoadBalancer, Ingress Controller, TLS Certificates, and HPA**.
---
## References and Official Documentation Resources
1. **Kubernetes & Docker**
   - Official Docs: https://kubernetes.io/docs/
   - kubectl Reference: https://kubernetes.io/docs/reference/kubectl/
   - Docker Reference: https://docs.docker.com/

2. **Ingress and Certificate Manager**
   - NGINX Ingress Controller: https://kubernetes.github.io/ingress-nginx/
   - Cert-Manager: https://cert-manager.io/docs/

3. **Horizontal Pod Autoscaler (HPA)**
   - HPA Documentation: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/

4. **Metrics Server**
   - Metrics Server Setup: https://github.com/kubernetes-sigs/metrics-server

5. **CI/CD and GitHub Actions**
   - GitHub Actions for Kubernetes: https://github.com/marketplace/actions/deploy-to-kubernetes-cluster

6. **Load Testing with k6**
   - k6 Documentation: https://grafana.com/docs/k6/latest/

7. **Flask**
   - Flask Documentation: https://flask.palletsprojects.com/en/stable/

8. **MongoDB Docs**
   - Official Documentation: https://www.mongodb.com/docs/

9. **DuckDNS**
   - Official Site: https://www.duckdns.org/
---
##  **Author:** Gaurav Kaushal
 **Date:** 25th March 2025

