# Course_work #1

import requests
import json
from datetime import datetime
import time
from tqdm import tqdm


class VKUser:
    method_url = 'https://api.vk.com/method/'

    def __init__(self, my_vk_token, version):
        self.params = {'access_token': my_vk_token, 'v': version}

    def get_photos(self, owner_id):
        get_photos_params = {
            'owner_id': owner_id,
            'album_id': 'profile',
            'rev': 0,
            'extended': 1,
            'photo_sizes': 1,
            'count': 1000
        }
        get_photos_url = self.method_url + 'photos.get'
        req = requests.get(get_photos_url, params = {**self.params, **get_photos_params}).json()
        items_list = req['response']['items']
        photo_dict = {}
        photos_json_dict = {}
        photos_json_list = []
        photo_likes_list = []

        for photo in items_list:
            photo_id = photo.get('id')
            photo_sizes = photo.get('sizes')
            photo_date = photo.get('date')
            photo_date = datetime.fromtimestamp(photo_date).strftime('%Y-%m-%d')
            largest_photo = photo_sizes[-1].get('url')
            type_size_photo = photo_sizes[-1].get('type')
            photo_likes = photo['likes']['count']

            if photo_likes in photo_likes_list:
                photo_dict[photo_id] = f'{photo_likes} - {photo_date}.jpg', largest_photo
                photo_likes_list.append(photo_likes)
            else:
                photo_dict[photo_id] = f'{photo_likes}.jpg', largest_photo
                photo_likes_list.append(photo_likes)

            photo_likes_json = f'{photo_likes}.jpg'
            photos_json_dict['filename'] = photo_likes_json
            photos_json_dict['size'] = type_size_photo
            photos_json_list.append(photos_json_dict)

        with open('photos_json.json', 'w') as outfile:
            json.dump(photos_json_list, outfile)

        progress_bar = tqdm(photo_dict.keys())
        for upload in progress_bar:
            time.sleep(0.5)
            progress_bar.set_description("Searching for photo_id %s" % upload)

        return photo_dict


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        self.headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def make_new_directory(self, directory_name):
        params = {'path': directory_name}
        requests.put(url = self.url, params = params, headers = self.headers)

    def upload_url(self, directory, uploading_urls_files):
        upload_url = self.url + 'upload'
        uploader.make_new_directory(directory)
        for values in uploading_urls_files.values():
            uploading_file_name = values[0]
            uploading_url_file = values[1]
            params = {"path": f'{directory}/{uploading_file_name}', 'url': uploading_url_file, "overwrite": "true"}
            response = requests.post(upload_url, params = params, headers = self.headers)

        progress_bar = tqdm(uploading_urls_files.keys())
        for upload in progress_bar:
            time.sleep(0.5)
            progress_bar.set_description("Uploading photo_id %s" % upload)


if __name__ == '__main__':

    def owner_id_request():
        while True:
            try:
                owner_id = int(input('Введите ID-Vkontakte (цифры) владельца фотографий (подсказка 552934290): '))
                return owner_id
            except ValueError:
                print("Вы ввели не число. Повторите ввод")

    def directory_name_request():
        directory_name = str(input('Введите название папки, в которую загрузить фотографии на Яндекс.Диск: '))
        return directory_name


    with open('/Users/artemstarodubtsev/PycharmProjects/pythonProject/Files/course_profile.txt', 'r') as file_object:
        file_object.readline()
        my_vk_token = file_object.readline().strip()
        file_object.readline()
        yandex_disk_token = file_object.readline().strip()

    directory = directory_name_request()
    owner_id = owner_id_request()
    vk_client = VKUser(my_vk_token, '5.131')
    urls_to_files = vk_client.get_photos(owner_id)
    uploader = YaUploader(yandex_disk_token)
    uploader.upload_url(directory, urls_to_files)