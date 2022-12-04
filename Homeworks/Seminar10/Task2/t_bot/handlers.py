
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from ui.ui_controller import *
from ui.ui_view import *

# (
#     MENU_CHOICE_STATE,
#     SHOW_EMPLOYEE_BY_ID_DEPARTMENT_STATE,
#     ADD_DEPARTMENT_STATE,
#     ADD_EMPLOYEE_STATE,
#     HIRE_EMPLOYEE_STATE,
#     MOVE_EMPLOYEE_STATE,
#     DISMISS_EMPLOYEE_STATE
#
# ) = range(7)

def menu_choice(update: Update, context: CallbackContext):
    um = update.message
    choice = int(um.text)
    if choice in (1, 2):
        if choice == 1: um.reply_text("СПИСОК ДЕПАРТАМЕНТОВ:")
        if choice == 2: um.reply_text("СПИСОК СОТРУДНИКОВ:")
        um.reply_text(ui.ui_controller.main(choice))
        um.reply_text("--------------")
        um.reply_text(ui.ui_controller.menu())
        return 1
    if choice == 3:
        um.reply_text("Введите ID отдела:")
        return 2
    if choice == 4:
        um.reply_text("Введите название отдела: ")
        return 3
    if choice == 5:
        um.reply_text(f"Введите имя сотрудника: ")
        return 4
    if choice == 6:
        um.reply_text(f"Введите ID сотрудника:")
        return 5
    if choice == 7:
        um.reply_text(f"Введите id сотрудника:")
        return 6
    if choice == 8:
        um.reply_text(f"Введите id сотрудника:")
        return 7
    if choice == 0:
        um.reply_text('Всего доброго! Для запуска программы: /start')
        return ConversationHandler.END


def show_employee_by_id_department(update: Update, context: CallbackContext):
    um = update.message
    id_dep = int(um.text)
    res = ui.ui_controller.main(3, id_dep)
    um.reply_text(f"СПИСОК СОТРУДНИКОВ В ДЕПАРТАМЕНТЕ С ID {id_dep}:")
    um.reply_text(res)
    if "{" in res:
        um.reply_text("--------------")
        um.reply_text(ui.ui_controller.menu())
        return 1
    else:
        um.reply_text("Введите ID отдела:")
        return 2

def new_department(update: Update, context: CallbackContext):
    um = update.message
    name_dep = um.text
    res = ui.ui_controller.main(4, name_dep)
    um.reply_text(f"Отдел {name_dep} успешно создан.")
    um.reply_text("--------------")
    um.reply_text(ui.ui_controller.menu())
    return 1

def new_employee(update: Update, context: CallbackContext):
    um = update.message
    if new_employee_form["stage"] == 0:
        new_employee_form["name"] = um.text
        um.reply_text(f"Введите размер заработной платы сотрудника: ")
        new_employee_form["stage"] = 1
        return 4
    if new_employee_form["stage"] == 1:
        new_employee_form["salary"] = int(um.text)
        ui.ui_controller.main(5, new_employee_form)
        um.reply_text("Сотрудник успешно создан")
        new_employee_form.clear()
        new_employee_form["stage"] = 0
        um.reply_text("--------------")
        um.reply_text(ui.ui_controller.menu())
        return 1

def hire_employee_handler(update: Update, context: CallbackContext):
    um = update.message
    if hire_employee_form["stage"] == 0:
        hire_employee_form["id_employee"] = int(um.text)
        um.reply_text("Введите id отдела для найма:")
        hire_employee_form["stage"] = 1
        return 5
    if hire_employee_form["stage"] == 1:
        hire_employee_form["id_department"] = int(um.text)
        res = ui.ui_controller.main(6, hire_employee_form)
        um.reply_text(res)
        hire_employee_form.clear()
        hire_employee_form["stage"] = 0
        um.reply_text("--------------")
        um.reply_text(ui.ui_controller.menu())
        return 1

def move_employee_handler(update: Update, context: CallbackContext):
    um = update.message
    if move_employee_form["stage"] == 0:
        move_employee_form["id_employee"] = int(um.text)
        um.reply_text("Введите id отдела для перевода:")
        move_employee_form["stage"] = 1
        return 6
    if move_employee_form["stage"] == 1:
        move_employee_form["id_department"] = int(um.text)
        res = ui.ui_controller.main(7, move_employee_form)
        um.reply_text(res)
        move_employee_form.clear()
        move_employee_form["stage"] = 0
        um.reply_text("--------------")
        um.reply_text(ui.ui_controller.menu())
        return 1

def dismiss_employee_handler(update: Update, context: CallbackContext):
    um = update.message
    id_emp = int(um.text)
    res = ui.ui_controller.main(8, id_emp)
    um.reply_text(res)
    um.reply_text("--------------")
    um.reply_text(ui.ui_controller.menu())
    return 1
