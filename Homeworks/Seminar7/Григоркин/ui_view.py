import action

MENU_ITEMS = {
   "1": "Поиск",
   "2": "Редактирование",
   "3": "Новый контакт",
   "4": "Удаление",
   "5": "Импорт",
   "6": "Экспорт",
   "0": "Выход"
}


def print_memory():
    print(f"Число в памяти: {action.memory}")


def menu():
    for index, item in MENU_ITEMS.items():
        print(f"{index} - {item}")
    print("Выберите пункт меню: ", end="")


def print_char(ch):
    print(f"Введите {ch}: ", end="")