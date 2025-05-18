import React, { useState } from "react";
import PredictionForm from "./components/PredictionForm";
import PredictionResult from "./components/PredictionResult";
import axios from "axios";
import "./App.css";

function App() {
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (formData) => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/predict", formData);
      setPrediction(response.data.predicted_price);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.detail || "An error occurred");
      setPrediction(null);
    }
  };

  return (
    <div className="App">
      <h1>Taxi Price Prediction</h1>
      <PredictionForm onSubmit={handleSubmit} />
      {prediction !== null && <PredictionResult prediction={prediction} />}
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default App;