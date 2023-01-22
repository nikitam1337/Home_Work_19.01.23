

def output_from():
    with open ('telephone_directory.txt', 'r') as data:
        for line in data:
            print(line)