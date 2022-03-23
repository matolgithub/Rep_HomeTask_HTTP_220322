import requests

import os

from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):  
        return {'Content-Type' : 'application/json', 'Authorization' : f'OAuth {self.token}'}

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на Яндекс-Диск"""

        file_path = os.path.normpath(file_path)
        data = {"file": open(file_path, 'rb')}
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path' : file_path, 'overwrite' : 'true'}
        response = requests.get(upload_url, params=params, headers=headers)
        href_json = response.json().get('href')
        response_upload = requests.put(url=href_json, files=data, headers={})
        pprint(response.json())
        print(f'The result of PUT-operation is: "{response_upload.status_code}". Successfuly!')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = "..."
    result = YaUploader(token).upload('1.txt')