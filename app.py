
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        try:
            if not city:
                error = "Please enter a city name."
            else:
                geo_response = requests.get(
                    GEOCODING_URL,
                    params={"name": city, "count": 1, "language": "en"},
                    timeout=10
                )
                geo_response.raise_for_status()
                results = geo_response.json().get("results", [])

                if not results:
                    error = "City not found."
                else:
                    location = results[0]

                    response = requests.get(
                        WEATHER_URL,
                        params={
                            "latitude": location["latitude"],
                            "longitude": location["longitude"],
                            "current": (
                                "temperature_2m,"
                                "relative_humidity_2m,"
                                "apparent_temperature,"
                                "weather_code,"
                                "wind_speed_10m"
                            ),
                            "timezone": "auto"
                        },
                        timeout=10
                    )
                    response.raise_for_status()

                    data = response.json()
                    current = data["current"]

                    codes = {
                        0: "Clear sky",
                        1: "Mainly clear",
                        2: "Partly cloudy",
                        3: "Overcast",
                        45: "Fog",
                        48: "Fog",
                        51: "Light drizzle",
                        53: "Drizzle",
                        55: "Heavy drizzle",
                        61: "Light rain",
                        63: "Rain",
                        65: "Heavy rain",
                        80: "Rain showers",
                        81: "Rain showers",
                        82: "Heavy rain showers",
                        95: "Thunderstorm"
                    }

                    weather = {
                        "city": location["name"],
                        "country": location.get("country", ""),
                        "temperature": current["temperature_2m"],
                        "humidity": current["relative_humidity_2m"],
                        "feels_like": current["apparent_temperature"],
                        "wind": current["wind_speed_10m"],
                        "description": codes.get(
                            current["weather_code"],
                            "Weather condition unavailable"
                        ),
                        "time": current["time"]
                    }

        except requests.RequestException:
            error = "Could not connect to the Weather API. Check your internet."

    return render_template(
        "index.html",
        weather=weather,
        error=error,
        city=city
    )


if __name__ == "__main__":
    app.run(debug=True)
