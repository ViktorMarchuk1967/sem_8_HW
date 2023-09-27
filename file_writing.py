"""Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной"""

"""Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также 
может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных и поиска 
по фамилии."""

from os.path import exists
from csv import DictReader, DictWriter


def get_info():
    info = []
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('wrong number')
            else:
                flag = True
        except ValueError:
            print('not valid number')
    info.append(phone_number)
    return info


def create_file():
    with open('phone.csv', 'w', encoding='utf-8') as data:
        # data.write('Фамилия;Имя;Номер\n')
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()


def write_file(lst):
    # with open('phone.txt', 'a', encoding='utf-8') as data:
    #     data.write(f'{lst[0]};{lst[1]};{lst[2]}\n')
    with open('phone.csv', 'r+', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
        print(res)
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        # res.append(obj)
        # print(res)
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writerow(obj)
        # for el in res:
        #     f_n_writer.writerow(el)


def read_file(file_name):
    # with open(file_name, encoding='utf-8') as data:
    #     phone_book = data.readlines()
    with open(file_name, encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book


def record_info():
    lst = get_info()
    write_file(lst)


def search_info():
    search_field = input('По какому полю ищем запись (n - имя, l - фамилия, t - телефон): ')
    search_el = input('Введите значение поля: ')
    find_num = -1
    with open('phone.csv', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
        for i in range(len(phone_book)):
            if ((search_field == 'n' or search_field == 'l') and (phone_book[i]['Фамилия'] == search_el or
                                                                  phone_book[i]['Имя'] == search_el)) or \
                    (search_field == 't' and int(phone_book[i]['Номер']) == int(search_el)):
                print(phone_book[i])
                find_num = i
                break
    return find_num


def update_info():
    find_num = search_info()
    if find_num > -1:
        phone_number = int(input('Введите новый номер телефона: '))
        with open('phone.csv', encoding='utf-8') as f_n:
            f_n_reader = DictReader(f_n)
            phone_book = list(f_n_reader)
            phone_book[find_num]['Номер'] = phone_number
        with open('phone.csv', 'w', encoding='utf-8') as data:
            # data.write('Фамилия;Имя;Номер\n')
            f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
            f_n_writer.writeheader()
            for el in phone_book:
                f_n_writer.writerow(el)


def delete_info():
    find_num = search_info()
    if find_num > -1:
        with open('phone.csv', encoding='utf-8') as f_n:
            f_n_reader = DictReader(f_n)
            phone_book = list(f_n_reader)
            phone_book.pop(find_num)
        with open('phone.csv', 'w', encoding='utf-8') as data:
            # data.write('Фамилия;Имя;Номер\n')
            f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
            f_n_writer.writeheader()
            for el in phone_book:
                f_n_writer.writerow(el)


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            print(read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()
        elif command == 's':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            else:
                find_num = search_info()
                if find_num == -1:
                    print("Запись не найдена")
        elif command == 'u':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            else:
                update_info()
        elif command == 'd':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            else:
                delete_info()


main()

