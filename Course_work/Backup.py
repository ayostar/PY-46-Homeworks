import os
import requests
from datetime import datetime
from progress.bar import Bar

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'AQAAAAAz55vbAAc-fohhPDQSvU5kroy21-HguNA'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def create_folder(path):
    """Создание папки. \n path: Путь к создаваемой папке."""
    requests.put(f'{URL}?path={path}', headers=headers)

def upload_file(loadfile, savefile, replace=False):
    """Загрузка файла.
    savefile: Путь к файлу на Диске
    loadfile: Путь к загружаемому файлу
    replace: true or false Замена файла на Диске"""
    res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    with open(loadfile, 'rb') as f:
        try:
            requests.put(res['href'], files={'file':f})
        except KeyError:
            print(res)

def backup(savepath, loadpath):
    """Загрузка папки на Диск. \n savepath: Путь к папке на Диске для сохранения \n loadpath: Путь к загружаемой папке"""
    date_folder = '{0}_{1}'.format(loadpath.split('\\')[-1], datetime.now().strftime("%Y.%m.%d-%H.%M.%S"))
    create_folder(savepath)
    for address, _, files in os.walk(loadpath):
        create_folder('{0}/{1}/{2}'.format(savepath, date_folder, address.replace(loadpath, "")[1:].replace("\\", "/")))
        bar = Bar('Loading', fill='X', max=len(files))
        for file in files:
            bar.next()
            upload_file('{0}\{1}'.format(address, file),\
                        '{0}/{1}{2}/{3}'.format(savepath, date_folder, address.replace(loadpath, "").replace("\\", "/"), file))
    bar.finish()


if __name__ == '__main__':
    #backup('Backup', r'C:\Files\backup')
    backup('Backup', os.getcwd())