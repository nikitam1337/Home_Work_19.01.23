

# def output_from():
#     with open ('telephone_directory.txt', 'r') as data:
#         for line in data:
#             print(line)
            
def output_from():
    list =[]
    with open ('telephone_directory.txt', 'r') as data:
        for line in data:
            list.append(line.replace('\n',''))
    return list