import requests
# twilio Recovery code: L6X6KRB9APDGVH7REDZ5YR2W
end_point = f"https://api.openweathermap.org/data/2.5/forecast"
api_key = "0322654e5c730c4d73d2c777d61917f1"
location = {
    "lon": 38.081408,
    "lat": 55.624584,
    "appid": api_key,
    "cnt": 4
}
# ?lat={lat}&lon={lon}&appid={API key}
response = requests.get(end_point, params=location)
data = response.json()
weather_id = []


weather0 = data["list"][0]["weather"][0]["id"]
weather1 = data["list"][1]["weather"][0]["id"]
weather2 = data["list"][2]["weather"][0]["id"]
weather3 = data["list"][3]["weather"][0]["id"]
if weather0 or weather1 or weather2 or weather3 < 700:
    print("bring an umbrella")

weather_id.append(weather0)
weather_id.append(weather1)
weather_id.append(weather2)
weather_id.append(weather3)

print(weather_id)


