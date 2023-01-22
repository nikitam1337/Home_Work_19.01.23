import view
import module_input as input
import module_output as out


def button_click():
    type = view.get_modul()
    if type==1: # Ввод данных
        user_input = view.get_string()
        print(user_input)
        input.input_in_file(user_input)
    if type ==0: # Вывод данных
        out.output_from()


