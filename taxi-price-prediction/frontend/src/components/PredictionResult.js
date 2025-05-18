import React from "react";

const PredictionResult = ({ prediction }) => {
  return (
    <div className="prediction-result">
      <h2>Predicted Price: ${prediction.toFixed(2)}</h2>
    </div>
  );
};

export default PredictionResult;