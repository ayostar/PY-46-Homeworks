# Course_work #1

with open('/Users/artemstarodubtsev/PycharmProjects/pythonProject/Files/course_profile.txt', 'r') as file_object:
    file_object.readline()
    my_vk_token = file_object.readline().strip()
    file_object.readline()
    owner_id = file_object.readline().strip()
    file_object.readline()
    client_id = file_object.readline().strip()
    file_object.readline()
    user_id = file_object.readline().strip()
    file_object.readline()
    yandex_disk_token = file_object.readline().strip()

import requests
from pprint import pprint
from datetime import datetime


class VKUser:
    method_url = 'https://api.vk.com/method/'

    def __init__(self, my_vk_token, version):
        self.params = {'access_token': my_vk_token,
                       'v': version}

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
        for photo in items_list:
            photo_id = photo.get('id')
            photo_sizes = photo.get('sizes')
            photo_date = photo.get('date')
            photo_date = datetime.fromtimestamp(photo_date).strftime('%Y-%m-%d')
            largest_photo = photo_sizes[-1].get('url')
            type_size_photo = photo_sizes[-1].get('type')
            photo_likes = photo['likes']['count']
            photo_dict[photo_id] = largest_photo, photo_likes, photo_date  ## Кортеж, а не список
        return photo_dict

        # photos_with_likes_dict = {}
        # for photo in items_list:
        #     photos_with_likes_dict[photo.get('id')] = photo.get('likes')
        # for values in photos_with_likes_dict.values():
        #     values.pop('user_likes')
        # for keys, values in photos_with_likes_dict.items():
        #     photos_with_likes_dict[keys] = values.get('count')
        #
        # photos_with_sizes_dict = {}
        # for photo in items_list:
        #     photos_with_sizes_dict[photo.get('id')] = photo.get('sizes')
        #
        # for photo_id, value in photos_with_sizes_dict.items():
        #     fat_photo = value[-1]
        #     photos_with_sizes_dict[photo_id] = fat_photo.get('url')

        # pprint(items_list)
        # pprint(photos_with_sizes_dict)

        # return photos_with_sizes_dict


# vk_client = VKUser(my_vk_token, '5.131')

# pprint(vk_client.get_photos(owner_id))


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        self.headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def make_new_directory(self, directory_name):
        params = {'path': directory_name}
        requests.put(url = self.url, params = params, headers = self.headers)

    def upload(self, directory, uploading_file: str):
        upload_url = self.url + 'upload'
        uploader.make_new_directory(directory)
        params = {"path": f'{directory}/{uploading_file}', "overwrite": "true"}
        response = requests.get(upload_url, headers = self.headers, params = params)
        response_dict = response.json()
        pprint(response_dict)

        href = response_dict.get("href", "")
        response = requests.put(href, data=open(uploading_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    def upload_url(self, directory, uploading_urls_files):
        upload_url = self.url + 'upload'
        uploader.make_new_directory(directory)
        for values in uploading_urls_files.values():
            uploading_url_file = values[0]
            uploading_file_name = values[1]
            params = {"path": f'{directory}/{uploading_file_name}.jpg', 'url': uploading_url_file, "overwrite": "true"}
            response = requests.post(upload_url, params = params, headers = self.headers)
        response_dict = response.json()
        pprint(response_dict)


if __name__ == '__main__':
    path_to_file = '1.txt'  ## список названий файлов
    vk_client = VKUser(my_vk_token, '5.131')
    urls_to_files = vk_client.get_photos(owner_id)
    pprint(vk_client.get_photos(owner_id))
    # urls_to_files = 'https://sun9-48.userapi.com/impg/hZBImqkCXbzy3VGIhn30Jj4P3RWurerkaZZSnw/oDCgWwpSe34.jpg?size=776x1080&quality=96&sign=dfa7e2744b632bcb9f98207fcbcd7e2e&c_uniq_tag=-OIhBF6MeG1Enc-LtRLB6cSUcbp87ZWbwyKmvMApZEM&type=album'  ## список url загружаемых файлов
    token = yandex_disk_token
    directory = 'Фото Шаляпы'
    uploader = YaUploader(token)
    # result = uploader.make_new_directory('Фото Шаляпы')  ## создание папки
    # result = uploader.upload(directory, path_to_file)
    result = uploader.upload_url(directory, urls_to_files)

# headers = {
#     "Accept": "application/json",
#     "Authorization": "OAuth " + token
# }
#
# params = {
#     'path': 'Test/d725774b8569795c8f4fc0c9c18ee9da.jpg',
#     'url': 'https://vk.com/begemot_korovin?z=photo552934290_457239029%2Fphotos552934290'
# }
#
# url = "https://cloud-api.yandex.net/v1/disk/resources/upload/"
# r = requests.post(url = url, params = params, headers = headers)
# res = r.json()
# print(json.dumps(res, sort_keys = True, indent = 4, ensure_ascii = False))