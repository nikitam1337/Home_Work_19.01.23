

def get_modul():
    while True:
        user_input = int(input(f'Выберите режим работы телефонного справочника:\n\
    Вывести данные из справочника --> введите 0\n\
    Записать данные в справочник --> введите 1.\n\
    ВЫХОД --> введите 2.\n\
    :'))
        if user_input ==1 or user_input==0 or user_input==2:
            return user_input
        else:
            print("Ошибка ввода!")

def get_string():
    id = input("Введите id: ")
    first_name = input('Введите Имя: ')
    last_name = input('Введите Фамилию: ')
    phone_number = input('Введите телефон: ')
    comment = input('Комментарий (по желанию): ')
    string = f"{id},{first_name},{last_name},{phone_number},{comment}"
    return string 

     #Строка содержит id,имя,фамилию,номер телефона, комментрий - 
        # символ разделитель на выбор(можно использовать пробел или запятые) +
        # файл с хранением этих строк