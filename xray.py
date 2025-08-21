from VPN_SERVICE import ABC_VPN_Service


class Xray(ABC_VPN_Service):

    def create_user_config(self):
        pass

    def edit_user_config(self):
        pass

    def recreate_user_config(self):
        pass

    def remove_user_config(self):
        pass

    def get_status_service(self):
        pass

    def start_service(self):
        pass

    def restart_service(self):
        pass

    def stop_service(self):
        pass

    def get_user_config(self):
        pass

    def get_all_users_configs(self):
        pass
