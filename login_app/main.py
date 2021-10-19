from inherited_classes import user as u
from inherited_classes import admin as a


def create_user():
    print("Enter first name: ")
    f_name = input()
    print("Enter last name: ")
    l_name = input()
    print("Enter age: ")
    age = int(input())
    print("Enter gender (M - male or F - female): ")
    gender = input()
    print("Enter id number: ")
    id_number = int(input())
    print("Enter Username: ")
    username = input()
    print("Enter Password: ")
    password = input()

    if gender == 'm' or gender == 'M':
        gender = 'Male'
    else:
        gender = 'Female'

    u.User(f_name, l_name, gender, username, password, age, id_number)


def create_admin():
    print("Enter first name: ")
    f_name = input()
    print("Enter last name: ")
    l_name = input()
    print("Enter age: ")
    age = int(input())
    print("Enter gender (M - male or F - female): ")
    gender = input()
    print("Enter id number: ")
    id_number = int(input())
    print("Enter Username: ")
    username = input()
    print("Enter Password: ")
    password = input()

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
