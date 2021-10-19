from core_classes import person as p


class Admin(p.Person):
    login_details = {}

    def __init__(self, first_name: str, last_name: str, gender: str, admin_username: str, admin_pin: int, age: int = 0,
                 id_number: int = 0):
        super().__init__(first_name, last_name, gender, age, id_number)

        self.admin_username = admin_username
        self.admin_pin = admin_pin

        Admin.login_details = {self.admin_username: self.admin_pin}
        Admin.admin_login_save_to_file(self)

    @staticmethod
    def admin_login_save_to_file(self):
        full_path = '/outputs'

        pass
