

def input_in_file(string):
    with open ('telephone_directory.txt', 'a') as data:
        data.write(f'{string}\n')
