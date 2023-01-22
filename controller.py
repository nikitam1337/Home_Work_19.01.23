import view
import module_input
import module_output


def button_click():
    type = view.get_modul()
    if type==1: # Ввод данных
        user_input = view.get_string()
        print(user_input)
        # Строка содержит id,имя,фамилию,номер телефона, комментрий - 
        # символ разделитель на выбор(можно использовать пробел или запятые) +
        # файл с хранением этих строк


