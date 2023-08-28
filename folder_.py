from datetime import datetime
import os
import shutil

# TARGET_FOLDER_PATH = 'E:'
TARGET_FOLDER_PATH = 'C:/Users/91755/Documents'
INPUT_FOLDER = 'C:/Users/91755/Desktop'
INVALID_EXTS = ['lnk', 'ini', 'exe']


def get_folder_name():
    t = str(datetime.now().replace(microsecond=0))
    replace_t = t.replace(':', '-')
    return replace_t


folder_name = get_folder_name()
folder_path = f'{TARGET_FOLDER_PATH}/{folder_name}'

if not os.path.exists(folder_path):
    os.mkdir(folder_path)  # make directory
    print(f'Created a folder: "{folder_path}"')


for file_ in os.listdir(INPUT_FOLDER):
    ext = file_.split('.')[-1]

    if ext in INVALID_EXTS:
        continue

    scr = f'{INPUT_FOLDER}/{file_}'
    dst = f"{folder_path}/{file_}"

    print(scr)

    if os.path.isfile(scr):
        shutil.copy(scr, dst)
    else:
        shutil.copytree(scr, dst)
