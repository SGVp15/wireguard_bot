from abc import ABC, abstractmethod


class ABC_VPN_Service(ABC):

    @abstractmethod
    def create_user_config(self):
        pass

    @abstractmethod
    def edit_user_config(self):
        pass

    @abstractmethod
    def recreate_user_config(self):
        pass

    @abstractmethod
    def remove_user_config(self):
        pass

    @abstractmethod
    def return_user_config(self):
        pass

    @abstractmethod
    def get_status_service(self):
        pass

    @abstractmethod
    def start_service(self):
        pass

    @abstractmethod
    def restart_service(self):
        pass

    @abstractmethod
    def stop_service(self):
        pass

    @abstractmethod
    def get_user_config(self):
        pass

    @abstractmethod
    def get_all_users_configs(self):
        pass
