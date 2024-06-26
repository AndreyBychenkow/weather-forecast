from urllib.parse import urlencode

import requests


def get_weather(city):
    base_url = "https://wttr.in/"
    params = {
        'lang': 'ru',
        'M': '',
        'u': '',
        'n': '',
        'q': '',
        'T': ''
    }
    url = f"{base_url}{city}?{urlencode(params)}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def main():
    cities = input("Введите город(а) через пробел: ").split()

    for city in cities:
        print(get_weather(city).capitalize())


if __name__ == '__main__':
    main()
