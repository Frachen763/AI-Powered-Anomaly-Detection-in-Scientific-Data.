# AI-Powered Anomaly Detection in Scientific Data

## Overview
This project is a **full-stack AI-powered anomaly detection system** designed for real-time scientific data monitoring.  
It leverages **PyTorch LSTM Autoencoders** to detect anomalies, a **FastAPI backend** for data ingestion & inference,  
**Supabase** for storage, and **Grafana** for real-time visualization.  
Built with CERN-like large-scale data environments in mind, it is optimized for streaming data and real-time dashboards.

---

## Tech Stack
- **Backend:** Python, FastAPI
- **Machine Learning:** PyTorch (LSTM Autoencoder)
- **Database & Auth:** Supabase
- **Visualization:** Grafana
- **Streaming:** WebSockets
- **Deployment:** Docker, docker-compose
- **CI/CD:** GitHub Actions

---

## Features
✅ Real-time anomaly detection from streaming data  
✅ LSTM Autoencoder for advanced time-series anomaly detection  
✅ Supabase integration for secure data storage and authentication  
✅ Grafana dashboard for live monitoring and analytics  
✅ Dockerized setup for quick deployment  
✅ CI/CD with GitHub Actions for automated testing and deployment  

---

## Architecture
```
                ┌───────────────────┐
                │ Data Generator     │
                └───────┬───────────┘
                        │ WebSockets
                ┌───────▼───────────┐
                │ FastAPI Backend   │
                │  - Model Inference│
                │  - API Endpoints  │
                └───────┬───────────┘
                        │
                ┌───────▼───────────┐
                │ Supabase Database │
                └───────┬───────────┘
                        │
                ┌───────▼───────────┐
                │ Grafana Dashboard │
                └───────────────────┘
```

---

## Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/anomaly-detection.git
cd anomaly-detection
```

### 2️⃣ Configure environment variables
Create a `.env` file in the root folder:
```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
MODEL_PATH=models/lstm_autoencoder.pth
```

### 3️⃣ Build & run using Docker
```bash
docker-compose up --build
```

### 4️⃣ Access the system
- **FastAPI Docs:** http://localhost:8000/docs
- **Grafana Dashboard:** http://localhost:3000

---

## Example Grafana Dashboard
![Grafana Example](docs/grafana_dashboard.png)

---

## Deployment
You can deploy this system on:
- **Render**
- **Heroku (via Docker)**
- **AWS ECS / Fargate**
- **DigitalOcean App Platform**

---

## Contributing
Pull requests are welcome! Please fork this repo and submit PRs with clear commit messages.

---

## License
This project is licensed under the MIT License.
