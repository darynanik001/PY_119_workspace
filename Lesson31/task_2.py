from typing import Any
import requests
import json


def dump_json(filename: str, data: Any) -> None:
    with open(f"{filename}.json", "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    url = "https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592&date=2023-01"
    response = requests.get(url)
    data = response.json()
    sorted_data = sorted(data, key=lambda item: item['id'])
    dump_json("data", sorted_data)
    print(type(sorted_data))
