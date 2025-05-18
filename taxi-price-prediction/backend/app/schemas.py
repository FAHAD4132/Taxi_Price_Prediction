from pydantic import BaseModel, Field
from enum import Enum

# Define enums for categorical fields
class TimeOfDay(str, Enum):
    MORNING = "Morning"
    AFTERNOON = "Afternoon"
    EVENING = "Evening"
    NIGHT = "Night"

class DayOfWeek(str, Enum):
    WEEKDAY = "Weekday"
    WEEKEND = "Weekend"

class TrafficConditions(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Weather_condition(str, Enum):
    CLEAR = "Clear"
    RAIN = "Rain"
    SNOW = "Snow"

# Define the input schema for the prediction API
class PredictionInput(BaseModel):
    """
    Schema for the input data required to make a prediction.
    """
    Trip_Distance_km: float = Field(..., gt=0, description="Trip distance in kilometers (must be positive)")
    Time_of_Day: TimeOfDay = Field(..., description="Time of day (Morning, Afternoon, Evening, Night)")
    Day_of_Week: DayOfWeek = Field(..., description="Day of the week (Weekday, Weekend)")
    Passenger_Count: float = Field(..., ge=1, description="Number of passengers (must be at least 1)")
    Traffic_Conditions: TrafficConditions = Field(..., description="Traffic conditions (Low, Medium, High)")
    Weather: Weather_condition = Field(..., description="Weather conditions (Clear, Rain, Snow)")
    Base_Fare: float = Field(..., gt=0, description="Base fare in local currency (must be positive)")
    Per_Km_Rate: float = Field(..., gt=0, description="Rate per kilometer in local currency (must be positive)")
    Per_Minute_Rate: float = Field(..., gt=0, description="Rate per minute in local currency (must be positive)")
    Trip_Duration_Minutes: float = Field(..., gt=0, description="Trip duration in minutes (must be positive)")

# Define the output schema for the prediction API
class PredictionOutput(BaseModel):
    """
    Schema for the output data returned by the prediction API.
    """
    predicted_price: float