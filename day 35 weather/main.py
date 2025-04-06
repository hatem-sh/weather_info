import requests
from typing import Dict, List, Optional
import os
from dotenv import load_dotenv

# Load environment variables (secure API key handling)
load_dotenv()

class WeatherForecast:
    """
    A class to fetch and analyze weather forecast data from OpenWeatherMap API.
    Checks if rain/snow is expected in the next 12 hours (4 intervals of 3-hour forecasts).
    """

    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, api_key: str, latitude: float, longitude: float):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude

    def _fetch_forecast(self) -> Optional[Dict]:
        """Fetch weather forecast data from OpenWeatherMap API."""
        params = {
            "lat": self.latitude,
            "lon": self.longitude,
            "appid": self.api_key,
            "cnt": 4  # Fetch next 12 hours (4x 3-hour intervals)
        }

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise HTTP errors if any
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def _will_it_rain_or_snow(self, weather_data: Dict) -> bool:
        """
        Check if rain/snow is expected in the forecast.
        Weather IDs < 700 indicate precipitation (rain, snow, etc.).
        """
        forecasts = weather_data.get("list", [])
        weather_ids = [
            forecast["weather"][0]["id"]
            for forecast in forecasts
            if forecast.get("weather")
        ]
        return any(weather_id < 700 for weather_id in weather_ids)

    def check_umbrella_needed(self) -> None:
        """Check if an umbrella is needed based on the forecast."""
        weather_data = self._fetch_forecast()
        if not weather_data:
            print("Failed to fetch weather data.")
            return

        if self._will_it_rain_or_snow(weather_data):
            print("Bring an umbrella! Rain or snow expected in the next 12 hours.")
        else:
            print("No umbrella needed. Clear skies ahead!")


if __name__ == "__main__":
    # Load API key from environment variables (secure)
    API_KEY = os.getenv("OPENWEATHER_API_KEY") or "your_api_key_here"
    
    # Example: Moscow coordinates
    weather = WeatherForecast(
        api_key=API_KEY,
        latitude=55.7558,
        longitude=37.6173
    )
    weather.check_umbrella_needed()
