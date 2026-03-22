import base64
import hashlib
import os
import re
from pathlib import Path


def to_md5(s: str):
    return hashlib.md5(s.encode()).hexdigest()


def clean_string(s: str) -> str:
    if type(s) is str:
        s = s.replace(',', ', ')
        s = re.sub(r'\s{2,}', ' ', s)
        s = s.strip()
    elif s in ('None', '#N/A', None):
        s = ''
    return s


def get_all_files_from_pattern(folder_input: str, pattern: str):
    file_list = []
    for root, dirs, files in os.walk(folder_input):
        for name in files:
            if name.endswith(pattern):
                file_list.append(os.path.join(root, name))
    return file_list


def file_to_base64(file_path_str: str) -> str:
    path = Path(file_path_str)

    if not path.exists():
        print(f"Ошибка: Путь '{path}' не существует.")
        return None
    if not path.is_file():
        print(f"Ошибка: '{path}' не является файлом.")
        return None

    try:
        file_bytes_data = path.read_bytes()

        # Кодируем в Base64
        base64_bytes = base64.b64encode(file_bytes_data)

        # Возвращаем строку
        return base64_bytes.decode('utf-8')

    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")
        return None
