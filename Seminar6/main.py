import calc_model
from ui_view import menu, print_char, print_memory
from ui_input import menu_input, check_menu_item, input_value, input_op


while True:
    print_memory()
    menu()
    menu_item = menu_input()
    if not (check_menu_item(menu_item)):
        continue
    print("Обработать далее...")
    print_char("a")
    a = input_value()
    print_char("b")
    b = input_value()
    calc_model.memory = calc_model.calculate(a, b, menu_item)
    print(f"Результат операции: {a} {menu_item} {b} = {calc_model.memory}")

