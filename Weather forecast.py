import requests


def main():
    urls = [
        'https://wttr.in/Лондон?lang=ru&M&u&n&q&T',
        'https://wttr.in/Шереметьево?lang=ru&M&u&n&q&T',
        'https://wttr.in/Череповец?lang=ru&M&u&n&q&T'
    ]

    for url in urls:
        response = requests.get(url)
        response.raise_for_status()

        print(response.text)


if __name__ == '__main__':
    main()
