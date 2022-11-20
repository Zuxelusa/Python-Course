from models import *

def input_check(input_str, min_val, max_val = 10000000):
    while True:
        val = input(input_str)
        if val.isdigit():
            val = int(val)
            if min_val <= val <= max_val:
                return int(val)
            else: print(f"Введите число от {min_val} до {max_val}")
        else:
            print(f"Введите число")
            continue

def prefix_menu():
    return print("\n\t\t\t\t\t ПРОГРАММА ДЛЯ РАБОТЫ С СОТРУДНИКАМИ ОТДЕЛОВ\n")

def menu_choice(max_menu):
    return input_check("Выберите пункт меню: ", 0, max_menu)

def show_departments():
    for department in departments:
        print(department)
    return "WATCH DEPARTMENTS"

def show_employees():
    for employee in employees:
        print(employee)
    return "WATCH EMPLOYEES"

def input_id_department():
    department_id = input_check("Введите id отдела: ", 1)
    if is_id(department_id, departments):
        show_employees_in_department(department_id)
        return f"WATCH EMPLOYEES IN DEPARTMENT ID {department_id}"
    else:
        print(f"Такого ID в базе не существует.")
        input_id_department()

def show_employees_in_department(id):
    department = [d for d in departments if d["id"] == id][0]
    for e_id in department["employees"]:
        print([e for e in employees if e["id"] == e_id])
    return f"WATCH EMPLOYEES IN DEPARTMENT ID {id}"

def input_name_department():
    new_dep = input("Введите название отдела: ")
    add_department(new_dep)
    return f"ADDED NEW DEPARTMENT {new_dep}"

def input_employee():
    name = input("Введите ФИО сотрудника: ")
    salary = input_check("Введите размер заработной платы сотрудника: ", 1, 500000)
    add_employee(name, salary)
    return f"ADDED NEW EMPLOYEE {name}"

def input_id_tohire():
    id_employee = input_check("Введите id сотрудника: ", 1)
    id_department = input_check("Введите id отдела для найма: ", 1)
    if not is_employee_in_department(id_employee, id_department):
        if is_id(id_department, departments) and is_id(id_employee, employees) :
            hire_employee(id_employee, id_department)
            print("Сотрудник успешно нанят")
            return f"HIRED EMPLOYEE ID {id_employee} IN DEPARTAMENT ID {id_department}"
        else:
            print(f"Такого(их) ID в базе не существует.")
            input_id_tohire()
    else:
        print("Этот сотрудник уже работает в указанном отделе")
        input_id_tohire()

def input_for_transfer():
    id_employee = input_check("Введите id сотрудника: ", 1)
    if is_id(id_employee, employees):
        lst = list((x["name"] for x in departments if id_employee in x["employees"]))
        print("Сотрудник будет переведен из отдела", lst[0])
        id_department = input_check("Введите id отдела для найма: ", 1)
        if is_id(id_department, departments):
            if not is_employee_in_department(id_employee,id_department):
                dep_cur = transfer_employee(id_employee, id_department)
                print("Сотрудник успешно переведен в", dep_cur)
                return f"TRANSFERED EMPLOYEE ID {id_employee} TO DEPARTAMENT ID {id_department}"
            else:
                print("Сотрудника не перевести, он уже работает в этом отделе.")
        else:
            print(f"Такого ID в базе не существует.")
    else:
        print(f"Такого ID в базе не существует.")
    input_for_transfer()

def input_for_dismiss():
    id_employee = input_check("Введите id сотрудника: ", 1)
    if is_id(id_employee, employees):
        lst = list((x["name"] for x in departments if id_employee in x["employees"]))
        print("Сотрудник будет уволен из отдела", lst[0])
        dismiss_emloyee(id_employee)
        print("Сотрудник успешно уволен")
        return f"EMPLOYEE ID {id_employee} DISMISSED"
    else:
        print(f"Такого ID в базе не существует.")
        input_for_dismiss()
