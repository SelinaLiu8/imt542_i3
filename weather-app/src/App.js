// App.js

import { useState } from "react";
import axios from "axios";
import './App.css';

export default function WeatherApp() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [forecast, setForecast] = useState(null);
  const [error, setError] = useState(null);

  const API_KEY = "368b0986ada24bb3b20213939251704";

  const getWeather = async () => {
    try {
      const weatherRes = await axios.get(
        `https://api.weatherapi.com/v1/current.json?key=${API_KEY}&q=${city}`
      );

      const forecastRes = await axios.get(
        `https://api.weatherapi.com/v1/forecast.json?key=${API_KEY}&q=${city}&days=7`
      );

      setWeather(weatherRes.data);
      setForecast(forecastRes.data.forecast.forecastday);
      setError(null);
    } catch (err) {
      setWeather(null);
      setForecast(null);
      setError("City not found or API error.");
    }
  };

  return (
    <div className="app_container">
      <div className="header">
        <h1 className="text-3xl font-bold mb-4">Weather App</h1>
      </div>
      <div className="search_container">
        <input
          type="text"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          placeholder="Enter city"
          className="p-2 border rounded-md"
        />
        <button
          onClick={getWeather}
          className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
        >
          Get Weather
        </button>
      </div>

      {error && <p className="text-red-600">{error}</p>}

      <div className="main_container">
        {weather && (
          <div className="current_container">
            <h2 className="text-xl font-semibold">
              {weather.location.name}
            </h2>
            <h3 className="text-xl font-semibold">
              {weather.location.country}
            </h3>
            <p className="text-lg">{weather.current.condition.text}</p>
            <p className="text-2xl">{weather.current.temp_c}°C</p>
          </div>
        )}

        {forecast && (
          <div className="forecast_container">
            <h3 className="forecast_title">7-Day Forecast</h3>
            <div className="forecast_list">
              {forecast.map((day) => (
                <div key={day.date} className="forecast_item">
                  <p className="font-semibold">{day.date}</p>
                  <p>{day.day.condition.text}</p>
                  <p>🌡️ {day.day.avgtemp_c}°C</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

