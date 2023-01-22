
def question ():
    flag = False
    while True:
        user_input = int(input(f'Хотите продолжить работу со справочником?\n\
    Продолжить --> введите 1\n\
    ВЫХОД --> введите 0.\n\
    :'))
        if user_input == 1:
            flag = True
            return flag
        elif user_input ==0:
            print('Завершение работы справочника.')
            break
        else:
            print("Ошибка ввода!")
    return flag