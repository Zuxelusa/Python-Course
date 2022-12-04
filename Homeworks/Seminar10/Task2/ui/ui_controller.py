from ui.ui_view import *
from ui.data_sr import *
from ui.logger import *

new_employee_form = {"stage": 0}
hire_employee_form = {"stage": 0}
move_employee_form = {"stage": 0}

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

def main(menu_number, param=None):
    read_data()
    result = MENU_ACTIONS[menu_number][1](param)
    save_data()
    if type(result) == tuple:
        log_add_note(result[1])
        return result[0]
    else:
        return result

def menu():
    menu_str = ""
    menu_str += prefix_menu()
    for key, value in MENU_ACTIONS.items():
        menu_str += f"{key} - {value[0]}\n"
    return menu_str

