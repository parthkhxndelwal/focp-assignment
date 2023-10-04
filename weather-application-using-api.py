import requests

# OpenWeatherMap API URL
api_key = "f03fce72033fd6d5335c0dddd4c1e911"
api_url = f"http://api.weatherstack.com/current"

# Function to fetch weather data
def get_weather_data(location):
    params = {
        "access_key": api_key,
        "query": location,
    }
    try:
        response = requests.get(api_url, params=params)
        data = response.json()
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to display weather forecast
def display_weather_data(data):
    if data is None:
        print("Failed to fetch weather data.")
        return

    location = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temperature"]
    description = data["current"]["weather_descriptions"][0]
    humidity = data["current"]["humidity"]
    wind_speed = data["current"]["wind_speed"]
    uv_index = data["current"]["uv_index"]

    print(f"Weather in {location}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")
    print(f"UV Index: {uv_index}")

# Main function to interact with the user
def main():
    print("Weather Forecast Checker")
    location = input("Enter a city or location: ")
    weather_data = get_weather_data(location)

    if weather_data:
        display_weather_data(weather_data)
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()