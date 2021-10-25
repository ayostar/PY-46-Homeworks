from pprint import pprint

import requests

TOKEN = ''

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers = headers, params = params)
        response_dict = response.json()
        pprint(response_dict)

        href = response_dict.get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    path_to_file = '1.txt'
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
