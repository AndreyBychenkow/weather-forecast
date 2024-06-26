import requests


def get_weather(city):
    base_url = f"https://wttr.in/{city}"
    params = {
        'lang': 'ru',
        'M': '',
        'u': '',
        'n': '',
        'q': '',
        'T': ''
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.text


def main():
    cities = input("Введите город(а) через пробел: ").split()

    for city in cities:
        print(get_weather(city).capitalize())


if __name__ == '__main__':
    main()
