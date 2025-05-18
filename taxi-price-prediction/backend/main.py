from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import PredictionInput, PredictionOutput
from app.models import preprocessing, prediction
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    try:
        # Convirt the input data to pandas data frame
        input_df = pd.DataFrame([{  'Trip_Distance_km': input_data.Trip_Distance_km,
                                    'Time_of_Day': input_data.Time_of_Day,
                                    'Day_of_Week': input_data.Day_of_Week,
                                    'Passenger_Count': input_data.Passenger_Count,
                                    'Traffic_Conditions': input_data.Traffic_Conditions,
                                    'Weather': input_data.Weather,
                                    'Base_Fare': input_data.Base_Fare,
                                    'Per_Km_Rate': input_data.Per_Km_Rate,
                                    'Per_Minute_Rate': input_data.Per_Minute_Rate,
                                    'Trip_Duration_Minutes': input_data.Trip_Duration_Minutes}]
                                )
        
        # Preprocess the input data
        processed_data = preprocessing(input_df)

        # Make prediction
        taxi_price_prediction = prediction(processed_data)

        # Return the prediction
        return PredictionOutput(predicted_price=float(taxi_price_prediction[0]))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    