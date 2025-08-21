import re
from pathlib import Path

from config import PATH_CONFIG, PATH_KEYS, PATH_QR
from utils.log import log


class UserConfig:
    """Класс для управления конфигурационными файлами, ключами и QR-кодами."""

    def __init__(self, file_name: str):
        """Инициализирует объект с указанным именем конфигурационного файла."""
        for directory in (PATH_CONFIG, PATH_KEYS, PATH_QR):
            if not Path.is_dir(directory):
                raise FileNotFoundError(f"Директория не найдена: {directory}")
        if not file_name.endswith('.conf'):
            raise ValueError("Имя файла должно заканчиваться на '.conf'")
        self.name = file_name[:-5]
        self.new_name = ''
        self.path_qr_file = Path(PATH_QR) / f'{self.name}.png'
        self.path_public_key = Path(PATH_KEYS) / f'{self.name}_public.key'
        self.path_private_key = Path(PATH_KEYS) / f'{self.name}_private.key'
        self.path_config_file = Path(PATH_CONFIG) / f'{self.name}.conf'

        self.address = ''
        self.public_key = ''
        if self.path_config_file.exists():
            try:
                with open(self.path_config_file, 'r') as f:
                    s = f.read()
                    matches = re.findall(r'Address\s*=\s*(\d+\.\d+\.\d+\.\d+/\d+)', s)
                    self.address = matches[0].strip() if matches else ''
            except (IOError, IndexError) as e:
                log.error(f"Ошибка при чтении конфигурационного файла: {e}")
        if self.path_public_key.exists():
            try:
                with open(self.path_public_key, 'r') as f:
                    self.public_key = f.read().strip()
            except IOError as e:
                log.error(f"Ошибка при чтении публичного ключа: {e}")

    def rename_conf(self, new_name: str) -> bool:
        """Переименовывает файлы конфигурации."""
        if not new_name or new_name == self.name:
            log.error("Новое имя не может быть пустым или совпадать с текущим")
            return False

        new_paths = [
            Path(PATH_CONFIG) / f'{new_name}.conf',
            Path(PATH_KEYS) / f'{new_name}_public.key',
            Path(PATH_KEYS) / f'{new_name}_private.key',
            Path(PATH_QR) / f'{new_name}.png'
        ]
        if any(p.exists() for p in new_paths):
            log.error(f"Файл с именем {new_name} уже существует")
            return False

        success = True
        for path in (self.path_private_key, self.path_public_key, self.path_config_file, self.path_qr_file):
            if path.exists():
                dist = path.parent / path.name.replace(self.name, new_name)
                try:
                    path.rename(dist)
                except (OSError, FileNotFoundError) as e:
                    log.error(f"Ошибка при переименовании {path}: {e}")
                    success = False
            else:
                log.warning(f"Файл не найден: {path}")

        if success:
            self.name = new_name
            self.path_qr_file = Path(PATH_QR) / f'{self.name}.png'
            self.path_public_key = Path(PATH_KEYS) / f'{self.name}_public.key'
            self.path_private_key = Path(PATH_KEYS) / f'{self.name}_private.key'
            self.path_config_file = Path(PATH_CONFIG) / f'{self.name}.conf'

        return success

    def delete_conf(self) -> bool:
        """Перемещает файлы конфигурации в корзину."""
        trash_dir = Path(PATH_CONFIG) / 'trash'
        trash_dir.mkdir(exist_ok=True)

        success = True
        for path in (self.path_private_key, self.path_public_key, self.path_config_file, self.path_qr_file):
            if path.exists():
                trash_path = trash_dir / path.name
                try:
                    path.replace(trash_path)
                except (OSError, FileNotFoundError) as e:
                    log.error(f"Ошибка при перемещении {path} в корзину: {e}")
                    success = False
            else:
                log.warning(f"Файл не найден: {path}")

        return success

    def return_conf(self) -> bool:
        """Восстанавливает файлы конфигурации из корзины."""
        success = True
        for path in (self.path_private_key, self.path_public_key, self.path_config_file, self.path_qr_file):
            trash_path = Path(path.parent) / 'trash' / path.name
            if trash_path.exists():
                try:
                    trash_path.replace(path)
                except (OSError, FileNotFoundError) as e:
                    log.error(f"Ошибка при восстановлении {trash_path}: {e}")
                    success = False
            else:
                log.warning(f"Файл не найден в корзине: {trash_path}")

        return success
