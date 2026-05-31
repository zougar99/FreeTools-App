#!/usr/bin/env python3
import json
import urllib.request
import urllib.parse

import os

API_KEY = os.environ.get("OWM_API_KEY", "")

def get_weather(city):
    if not API_KEY:
        return "API key not configured. Please set API_KEY in the code."
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            return f"{data['name']}: {data['main']['temp']}°C, {data['weather'][0]['description']}"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=" * 50)
    print("       WEATHER")
    print("=" * 50)
    
    city = input("City name: ")
    result = get_weather(city)
    print(f"\n{result}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()