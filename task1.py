"""Задача №49. Решение в группах
Создать телефонный справочник с
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
не должна быть линейной
"""
def read_txt(filename,fields):
    phone_book=[]
    with open(filename, 'r',encoding='utf-8') as phb:
        for line in phb:
            line = list(map(str.strip,line.split(',')))
            record = dict(zip(fields, line))
            phone_book.append(record)
    return(phone_book)

def print_result(phone_book):
    for i in phone_book :
        print(', '.join([f'{key}: {value}' for key, value in i.items()]))


def find_by_lastname(phone_book,last_name):
    for dct in phone_book:
        if "Фамилия" in dct and dct["Фамилия"] == last_name:
            return dct.get('Телефон',0)

def write_txt(filename, phone_book):
    with open(file_phone,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

def change_number(phone_book,last_name,new_number):
    for dct in phone_book:
        if "Фамилия" in dct and dct["Фамилия"] == last_name:
            old_num = dct['Телефон']
            dct['Телефон'] = new_number
            write_txt(file_phone, phone_book)
            rec_ = 'Номер ' + old_num + ' заменен на ' + dct.get('Телефон',0)
            return rec_

def delete_by_lastname(phone_book,last_name):
    for dct in phone_book:
        if "Фамилия" in dct and dct["Фамилия"] == last_name:
            lst = list(dct.values())
            del_rec = ', '.join(lst)
            phone_book.remove(dct)    
            write_txt(file_phone, phone_book)
            return(print(f'Запись: ', del_rec, 'удалена из справочника'))
        
def find_by_number(phone_book,number):
    for dct in phone_book:
        if str(dct["Телефон"]) == number:
            abonent = dct.get('Фамилия',0) + ' ' + dct.get('Имя',0)
            return abonent
        
def add_user(phone_book,user_data,fields):
    record = dict(zip(fields, user_data))
    phone_book.append(record)
    return(phone_book)

    
def work_with_phonebook():
    choice=show_menu()
    phone_book = read_txt(file_phone,fields)
    if choice in range (1,7):
        while (choice!=7):
            if choice==1:
                print_result(phone_book)
            elif choice==2:
                last_name=input('Введите фамилию абонента -> ')
                print(find_by_lastname(phone_book,last_name))
            elif choice==3:
                last_name=input('Введите фамилию абонента -> ')
                new_number=input('Введите новый номер телефона -> ')
                print(change_number(phone_book,last_name,new_number))
            elif choice==4:
                last_name=input('Введите фамилию удаляемого абонента -> ')
                print(delete_by_lastname(phone_book,last_name))
            elif choice==5:
                number=input('Введите номер для поиска абонента -> ')
                print(find_by_number(phone_book,number))
            elif choice==6:
                user_data = [input('Введите фамилию абонента -> '),
                                 input('Введите имя абонента -> '),
                                 input('Введите телефон абонента -> '),
                                 input('Введите описание абонента -> ')]
                add_user(phone_book,user_data,fields)
                write_txt(file_phone,phone_book)
            else: exit
            choice=show_menu()

def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента в справочнике',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', sep = '\n')
    choice = int(input('Введите номер команды -> '))
    return(choice)



fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
file_phone = 'phonebook.txt'
work_with_phonebook()