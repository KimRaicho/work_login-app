from inherited_classes import user as u
from inherited_classes import admin as a


def create_user():
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender (M - male or F - female): ")
    id_number = int(input("Enter id number: "))
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if gender == 'm' or gender == 'M':
        gender = 'Male'
    else:
        gender = 'Female'

    u.User(f_name, l_name, gender, username, password, age, id_number)


def create_admin():
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender (M - male or F - female): ")
    id_number = int(input("Enter id number: "))
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if gender == 'm' or gender == 'M':
        gender = 'Male'
    else:
        gender = 'Female'

    a.Admin(f_name, l_name, gender, username, password, age, id_number)


def menu():
    print('=======================ROBOT APPLICATION========================')

    option = 0

    while option != 3:
        print('''
1. USER
2. ADMIN
3. QUIT ''')

        print(f'option: ')
        option = int(input())

        if option == 1:
            create_user()
        elif option == 2:
            create_admin()
        else:
            print('GOODBYE!')


if __name__ == '__main__':
    menu()
