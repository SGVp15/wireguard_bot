import base64
from pathlib import Path


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


if __name__ == "__main__":
    file_path = './data/log.txt'

    base64_output = file_to_base64(file_path)

    if base64_output:
        # Для удобства выводим только первые 100 символов, если строка очень длинная
        print("\n--- Результат Base64 (начало строки) ---")
        print(base64_output[:100] + "...")
        print("---------------------------------------")
        print(f"Полная длина: {len(base64_output)} символов.")
