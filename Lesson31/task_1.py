import requests

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Robot"
    response = requests.get(url)
    if response.status_code == 200:
        text_data = response.text
        with open("robots.txt", "w", encoding="UTF-8") as f:
            f.write(str(text_data))
    else:
        print(f"Impossible to retrieve content from {url}. Status code: {response.status_code}")
