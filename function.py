# Часть проверки ввода данных, и вывода данных (требуют доработок)
import datetime

def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(15), "Имя".center(15), "Отчество".center(15), "Дата рождения".center(15), "Телефон".center(15), "Пол".center(20), "Дата и Время внесения".center(20))
        print("-"*125)
        for item in data:
            print(item[0].center(15), item[1].center(15), item[2].center(15), item[3].center(15), item[4].center(15), item[5].center(20), item[6].center(20))
    else:
        print("Справочник пуст!")

'''функция проверки на ввод только букв'''
def correct_input(text):
    name = input(f'{text} > ')
    if name == '*':
        return name 
    while not name.isalpha():
        print('Вы вводите что-то, кроме букв. Вводите только буквы: ')
        name = input(f'{text} > ')
    return name.upper()    

'''функция проверки номера'''
def correct_number(text):
    number = input(f'{text} > ')
    while True:
        if number.isdigit() and len(number) == 11:
            return number
        if not number.isdigit():
            print('Вы ввели номер телефона с символами, не являющимися цифрами. Введите номер формата 79876543211: ')
        if len(number) > 11:
            print('Вы ввели номер большего размера, чем обычный. Введите номер формата 79876543211: ')
        if len(number) < 11:
            print('Вы ввели номер меньшего размера, чем обычный. Введите номер формата 79876543211: ')
        number = input(f'{text} > ')

'''функция проверки года рождения'''        
def correct_age(text):
    age = input(f'{text} > ')
    while True:
        if len(age) == 10:
            return age
        if len(age) > 10:
            print('Количество символов в дате рождения больше требуемого. Введите правильную дату рождения формата dd.mm.yyyy')
        if len(age) < 10:
            print('Количество символов в дате рождения меньше требуемого. Введите правильную дату рождения формата dd.mm.yyyy')
        age = input(f'{text} > ')
        
'''функция проверки пола'''        
def correct_gender(text):
    gender = input(f'{text} > ').upper()
    while True:
        if gender == 'F' or gender == 'M':
            return gender
        else:
            print('Не корректный ввод. Введите F или M: ')
            gender = input(f'{text} > ').upper()
    

''' функция получения данных'''        
def data_input(listfields):
    list_fun = [correct_input, correct_input, correct_input, correct_age, correct_number, correct_gender]
    return [fun(text) for text, fun in zip(listfields, list_fun)]  
     