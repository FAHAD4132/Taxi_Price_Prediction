import joblib
import os
import numpy as np
import pandas as pd
from fastapi import HTTPException

# Load the trained model, scaler and OneHotEncoder
def load_model():
    """
    Load the trained machine learning model.
    """
    model_path = os.path.join(os.path.dirname(__file__), "taxi_price_prediction_ensemble_model.pkl")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    return joblib.load(model_path)


def load_scaler():
    """
    Load the scaler.
    """
    scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")
    if not os.path.exists(scaler_path):
        raise FileNotFoundError(f"Scaler file not found at {scaler_path}")
    return joblib.load(scaler_path)

def load_encoder():
    """
    Load the encoder.
    """
    encoder_path = os.path.join(os.path.dirname(__file__), "one_hot_encoder.pkl")
    if not os.path.exists(encoder_path):
        raise FileNotFoundError(f"Encoder file not found at {encoder_path}")
    return joblib.load(encoder_path)


def preprocessing(input_df):
    try:
        # Load the saved encoder
        encoder = load_encoder()

        # One-Hot Encoding categorical variables
        categorical_cols = input_df.select_dtypes(include=['object']).columns
        encoded_array = encoder.transform(input_df[categorical_cols])

        # Create a DataFrame with encoded columns
        encoded_df = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out(categorical_cols))
        encoded_df = encoded_df.astype(int)

        # Drop original categorical columns and concatenate new one-hot encoded columns
        input_df = input_df.drop(columns=categorical_cols).reset_index(drop=True)
        input_df = pd.concat([input_df, encoded_df], axis=1)

        # Load the saved scaler
        scaler = load_scaler()

        X_scaled = input_df.copy()
        X_scaled[input_df.select_dtypes(include=["float"]).columns] = scaler.transform(input_df[input_df.select_dtypes(include=["float"]).columns])

        return X_scaled
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def prediction(X):
    try:
        model = load_model()

        # Make predictions
        result = model.predict(X)

        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))