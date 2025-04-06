🔧 Features
API Integration: Fetches real-time weather data from OpenWeatherMap.

Precipitation Check: Detects rain, snow, or other adverse weather conditions (weather ID < 700).

Error Handling: Gracefully manages API failures or missing data.

Secure Key Management: Uses environment variables (python-dotenv) to protect API keys.

Modular & Scalable: Structured as a reusable Python class for easy extension.
-----------------------------------------------------------------------------------------------

🛠️ Technologies
Python 3

requests (HTTP API calls)

python-dotenv (secure API key storage)

OpenWeatherMap API
----------------------------------------------------------------------------------------------
🚀 Setup
1- Clone the repo:
git clone https://github.com/your-username/weather-forecast-checker.git


2- Install dependencies:
pip install requests python-dotenv


3- Add your OpenWeatherMap API key to .env:
OPENWEATHER_API_KEY=your_api_key_here


4- Run the script:
python weather_checker.py
