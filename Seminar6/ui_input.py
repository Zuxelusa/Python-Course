from ui_view import MENU_ITEMS

def menu_input():
    menu_item = input()
    return menu_item

def check_menu_item(menu_item):
    return bool(MENU_ITEMS.get(menu_item))

def input_value():
    return int(input())

def input_op():
    return input()
