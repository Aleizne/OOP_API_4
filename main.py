# Задание №1
import requests


def detect_intelligence(heroes_names: list) -> dict:
    heroes_dict = {}
    for hero_name in heroes_names:
        url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
        response = requests.get(url=url)
        hero_data = response.json()
        for item in hero_data:
            if hero_name in item['name']:
                heroes_dict[hero_name] = item['powerstats']['intelligence']
    return heroes_dict


def smartest_one(targets: list) -> None:
    to_compare = detect_intelligence(targets)
    champion = max(to_compare, key=to_compare.get)
    print(f'{champion} has the highest intelligence score! It is {to_compare[champion]}!!!')


# Задание №2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_link(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'OAuth {self.token}'
        }
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

        def upload(self, file_path: str):
        href = self.get_link(file_path=file_path).get("href", "")
        with open(file_path, 'rb') as f_path:
            response = requests.put(href, data=f_path)
            response.raise_for_status()
            if response.status_code == 201:
                print("File was succesfully uploaded.\nCheck it in your yaDisk ;)")

    # Тут ваша логика(зачеркнуто) магия. Убежден что моя чашка кофе... чая... понимает как это работает лучше меня.


if __name__ == '__main__':

    # Проверяем и выполняем задание №1
    target_list = ['Hulk', 'Captain America', 'Thanos']
    smartest_one(target_list)

    # Проверяем и выполняем задание №2
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
