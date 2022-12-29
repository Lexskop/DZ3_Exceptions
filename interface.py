from import_export import write_data
from import_export import read_data
from controller import*
from function import print_data
import csv

# Часть для ввода команд

def select_operation():
    while True:
        print("Добро пожаловать в телефонный справочник!")
        print('''\nКоманды выбора меню для работы со справочником:
        1 - Добавить контакт 
        0 - Выход.\n''')

        menu_selection = input('Введите номер меню: > ')

        if menu_selection == '1':
            list_add=input_data()
            write_data(list_add,sep=",")
        elif menu_selection == '0':
            print("Работа завершена")
            raise SystemExit