import view
import module_input as input
import module_output as out
import continue_question as question


def button_click():
    type = view.get_modul()
    if type == 1:  # Ввод данных
        flag = True
        while flag:
            user_input = view.get_string()
            input.input_in_file(user_input)
            flag = question.question()
    if type == 0:  # Вывод данных   содержит id,имя,фамилию,номер телефона, комментрий - 
        output_list = out.output_from()
        if len(output_list)==0:
            print("В справочнике нет записей. Запустите режим ввода данных!")
        else:
            title = ['id:','Имя:','Фамилия:','Номер телефона:','Комментарий:']
            for i in range(len(output_list)):
                result = list(zip(title,output_list[i].split(',')))
                print(result)
    if type == 2:
        print('Завершение работы справочника.')
