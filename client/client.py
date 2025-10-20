import requests


def main():
    try:
        print("Делаем запрос на сервер...")
        response = requests.get('http://server:8000/file')
        response.raise_for_status()
        print("Получили текстовое сообщение:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    main()
