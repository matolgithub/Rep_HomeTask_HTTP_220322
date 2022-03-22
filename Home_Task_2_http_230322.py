import requests

from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать

    def get_headers(self):
        return {'Content-Type' : 'application/json', 'Authorization' : 'OAuth {}'.format(self, token)}

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = "AQAAAAANuuWFAADLW1koNP7ciknerimibi-F350"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

    # token = "AQAAAAANuuWFAADLW1koNP7ciknerimibi-F350"
   
