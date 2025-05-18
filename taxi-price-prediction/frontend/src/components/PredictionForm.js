import React, { useState } from "react";

const PredictionForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    Trip_Distance_km: 1,
    Time_of_Day: "Morning",
    Day_of_Week: "Weekday",
    Passenger_Count: 1,
    Traffic_Conditions: "Low",
    Weather: "Clear",
    Base_Fare: 1,
    Per_Km_Rate: 1,
    Per_Minute_Rate: 1,
    Trip_Duration_Minutes: 1,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="prediction-form">
      <div>
        <label>Trip Distance (km):</label>
        <input
          type="float"
          name="Trip_Distance_km"
          value={formData.Trip_Distance_km}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Time of Day:</label>
        <select
          name="Time_of_Day"
          value={formData.Time_of_Day}
          onChange={handleChange}
        >
          <option value="Morning">Morning</option>
          <option value="Afternoon">Afternoon</option>
          <option value="Evening">Evening</option>
          <option value="Night">Night</option>
        </select>
      </div>
      <div>
        <label>Day of Week:</label>
        <select
          name="Day_of_Week"
          value={formData.Day_of_Week}
          onChange={handleChange}
        >
          <option value="Weekday">Weekday</option>
          <option value="Weekend">Weekend</option>
        </select>
      </div>
      <div>
        <label>Passenger Count:</label>
        <input
          type="float"
          name="Passenger_Count"
          value={formData.Passenger_Count}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Traffic Conditions:</label>
        <select
          name="Traffic_Conditions"
          value={formData.Traffic_Conditions}
          onChange={handleChange}
        >
          <option value="Low">Low</option>
          <option value="Medium">Medium</option>
          <option value="High">High</option>
        </select>
      </div>
      <div>
        <label>Weather:</label>
        <select
          name="Weather"
          value={formData.Weather}
          onChange={handleChange}
        >
          <option value="Clear">Clear</option>
          <option value="Rain">Rain</option>
          <option value="Snow">Snow</option>
        </select>
      </div>
      <div>
        <label>Base Fare:</label>
        <input
          type="float"
          name="Base_Fare"
          value={formData.Base_Fare}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Per Km Rate:</label>
        <input
          type="float"
          name="Per_Km_Rate"
          value={formData.Per_Km_Rate}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Per Minute Rate:</label>
        <input
          type="float"
          name="Per_Minute_Rate"
          value={formData.Per_Minute_Rate}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Trip Duration (Minutes):</label>
        <input
          type="float"
          name="Trip_Duration_Minutes"
          value={formData.Trip_Duration_Minutes}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit">Predict Price</button>
    </form>
  );
};

export default PredictionForm;