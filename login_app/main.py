from core_classes import person as p
from inherited_classes import user as u


def create_person():
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

    if gender == 'm' or gender == 'M':
        gender = 'Male'
    else:
        gender = 'Female'

    p.Person(f_name, l_name, gender, age, id_number)
    p.Person.save_to_file()


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


if __name__ == '__main__':
    # create_person()
    # print(f'\n Person Created: {p.Person.people}')

    create_user()
