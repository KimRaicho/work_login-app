from core_classes import person as p
import os


class User(p.Person):
    login_details = {}

    def __init__(self, first_name: str, last_name: str, gender: str, username, password, age: int = 0,
                 id_number: int = 0):
        super().__init__(first_name, last_name, gender, age, id_number)

        self.username = username
        self.password = password

        User.login_details = {self.username: self.password}
        User.user_login_save_to_file(self)

    @staticmethod
    def user_login_save_to_file(self):
        full_path = '/outputs'

        if not os.path.isfile(full_path + '/user_login.txt'):
            file = open(full_path + '/user_login.txt', 'a')
            file.writelines('USERNAME \t\t' + 'PASSWORD \n')

            for username, password in User.login_details:
                file.write(username + '\t\t\t')
                file.write(password + '\t\t\t')
