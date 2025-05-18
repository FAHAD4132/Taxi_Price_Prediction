# Taxi Price Prediction System

A full-stack machine learning application that accurately predicts taxi fares based on trip parameters. This system combines a FastAPI backend with a trained ensemble model and a React.js frontend.

![image](https://github.com/user-attachments/assets/b39b0906-9252-49ca-9dbf-39a55eb62eb5)

A full-stack application that predicts taxi fares based on various trip parameters, featuring:
- **Backend**: FastAPI service with machine learning model
- **Frontend**: React.js user interface
- **Containerized**: Docker and Docker Compose setup

## Features

- Predict taxi prices based on:
  - Trip distance and duration
  - Time of day and day of week
  - Passenger count
  - Traffic and weather conditions
  - Fare rates
- Responsive web interface
- REST API endpoint for predictions
- Containerized deployment

## Technologies

**Backend**:
- Python 3.9
- FastAPI
- Scikit-learn (for model)
- Pandas
- Joblib

**Frontend**:
- React.js
- Axios
- CSS

**Infrastructure**:
- Docker
- Docker Compose
- Nginx (for frontend serving)

## Prerequisites

- Docker (v20.10+)
- Docker Compose (v2.0+)
- Node.js (v16+) - only for frontend development
- Python (v3.9+) - only for backend development

## Installation

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/FAHAD4132/Taxi-Price-Prediction.git
   cd taxi-price-prediction

2. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Manual Setup (Development)

**Backend**:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend**:
```bash
cd frontend
npm install
npm start
```

## Project Structure

```
taxi-price-prediction/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py                                        # ML model loading and prediction
│   │   ├── schemas.py                                       # Pydantic models
│   │   ├── scaler.pkl                                       # StandardScaler
│   │   ├── one_hot_encoder.pkl                              # OneHotEncoder
│   │   ├── taxi_price_prediction_ensemble_model.pkl         # ML model
│   ├── main.py                                              # FastAPI app
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── App.js             # Main app component
│   │   └── ...                # Other React files
│   ├── Dockerfile
│   └── package.json
└── docker-compose.yml
```

## API Documentation

The backend provides automatic API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Endpoints

**POST /predict**
- Request body: See `PredictionInput` schema
- Response: `PredictionOutput` with predicted price

## Usage

1. Open the frontend at http://localhost:3000
2. Fill in the trip details:
   - Distance, duration, passenger count
   - Select time, day, traffic and weather conditions
   - Enter fare rates
3. Click "Predict Price"
4. View the predicted fare

## Acknowledgments

- FastAPI for the excellent Python web framework
- React.js for the frontend framework
- Scikit-learn for machine learning tools
