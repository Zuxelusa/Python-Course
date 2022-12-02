
from telegram import Update
from telegram.ext import CallbackContext
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
    # if choice == 5:
    # if choice == 6:
    # if choice == 7:
    # if choice == 8:
    # if choice == 0:


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
    # um.reply_text(f"СПИСОК СОТРУДНИКОВ В ДЕПАРТАМЕНТЕ С ID {id_dep}:")
    # um.reply_text(res)
    # if "{" in res:
    #     um.reply_text("--------------")
    #     um.reply_text(ui.ui_controller.menu())
    #     return 1
    # else:
    #     um.reply_text("Введите ID отдела:")
    #     return 2
