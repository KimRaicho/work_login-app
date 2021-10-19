from core_classes import person as p
import os


class Admin(p.Person):
    login_details = {}

    def __init__(self, first_name: str, last_name: str, gender: str, admin_username, admin_password, age: int = 0,
                 id_number: int = 0):
        super().__init__(first_name, last_name, gender, age, id_number)

        self.admin_username = admin_username
        self.admin_password = admin_password

        Admin.login_details = {self.admin_username: self.admin_password}
        Admin.admin_login_save_to_file()

    @staticmethod
    def admin_login_save_to_file():
        full_path = 'C:\\Users\\Raicho\\Desktop\\work Final project\\outputs'

        if not os.path.isfile(full_path + '/admin_login.txt'):
            file = open(full_path + '/admin_login.txt', 'a')
            file.writelines('USERNAME \t\t' + 'PASSWORD \n')

            for username, password in Admin.login_details.items():
                file.write(username + '\t\t\t')
                file.write(password + '\t\t\t')
