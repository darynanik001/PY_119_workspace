import requests

API_KEY = "2d153ad26e0133a5cdb906f91e107bdd"


def get_weather_info_by_city(city: str, limit: int = 5) -> str:
    response = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={API_KEY}")
    return response.json()


if __name__ == "__main__":
    print(get_weather_info_by_city("Kyiv"))
