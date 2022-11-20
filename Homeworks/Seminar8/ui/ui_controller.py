from ui.ui_view import *
from ui.data_sr import *
from ui.logger import *

MENU_ACTIONS = {
    1: ["Вывести список отделов", show_departments],
    2: ["Вывести список всех сотрудников", show_employees],
    3: ["Вывести список сотрудников отдела (по номеру)", input_id_department],
    4: ["Добавить отдел", input_name_department],
    5: ["Добавить сотрудника", input_employee],
    6: ["Нанять сотрудника", input_id_tohire],
    7: ["Переместить сотрудника в другой отдел", input_for_transfer],
    8: ["Уволить сотрудника", input_for_dismiss],
    0: ["Выход", 0]
}

def main():
    read_data()
    menu_number = 1
    while menu_number:
        menu_number = menu()
        if menu_number > 0:
            note = MENU_ACTIONS[menu_number][1]()
            save_data()
            log_add_note(note)

def menu():
    prefix_menu()
    for key, value in MENU_ACTIONS.items():
        print(key, value[0], sep=" - ")
    return menu_choice(max(MENU_ACTIONS.keys()))




