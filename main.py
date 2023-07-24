
book_dict = {}

# чтение
# def read_phonebook():
#     with open('phonebook/phonebook','r', encoding='UTF-8') as file:
#         data = file.read()
#     return data

# print(read_phonebook())

# добавление
# def add_contact(name,number):
#     with open('phonebook/phonebook','a', encoding='UTF-8') as file:
#         book_dict[name] = number
#     return book_dict

# print(add_contact('RAZ', 123))

# поиск
def find_contact(name):
    with open('phonebook/phonebook','r', encoding='UTF-8') as fh:
        for i in fh.readlines():
            if i:
                key, val = i.strip().split(':')
                book_dict[key] = val
        for i in book_dict.keys():
            if i == name:
                return f"{i} - {book_dict[i]}"
            else:
                return "Контакт не найден"
            
print(find_contact('Роберт'))
