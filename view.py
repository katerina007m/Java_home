import text

def show_menu() -> int:
    for i, item in enumerate(text.main_menu):
        if i:
            print('\t' + f'{i}. {item}')
        else:
            print(item)
    select_option = input('Выберите пункт меню: ')
    while True:
        if select_option.isdigit() and 0 < int(select_option) < len(text.main_menu) - 1:
            return  int(select_option)
        select_option = input(text.main_menu_input_error)

def show_contact(book: dict[int, list[str]], msg:str):
    print('\n' + '='*67)
    if book:
        for uid, contact in book.items():
            print(f'{uid: >3}. {contact[0]: <20} {contact[1]: <20} {contact[2]: <20}')
    else:
        print(msg)
    print('=' * 67 + '\n')

def print_msg(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')

def input_new_contact(input_list: list[str]):
    new_contact = []
    for item in input_list:
        new_contact.append(input(item))
    return new_contact

def input_data(msg: str) -> str:
    return input(msg)

