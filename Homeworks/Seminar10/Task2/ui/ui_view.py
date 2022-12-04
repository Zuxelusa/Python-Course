import ui.ui_controller
from models import *

def prefix_menu():
    return "\n\t\t\t\t\t ПРОГРАММА ДЛЯ РАБОТЫ С СОТРУДНИКАМИ ОТДЕЛОВ\n"


def show_departments(param = None):
    res = ""
    for department in ui.ui_controller.departments:
        res += f"{department}\n"
    return res, "WATCH DEPARTMENTS"

def show_employees(param = None):
    res = ""
    for employee in ui.ui_controller.employees:
        res += f"{employee}\n"
    return res, "WATCH EMPLOYEES"

def input_id_department(department_id):
    if is_id(department_id, ui.ui_controller.departments):
        return show_employees_in_department(department_id), f"WATCH EMPLOYEES IN DEPARTMENT ID {department_id}"
    else:
        return f"Такого ID в базе не существует."

def show_employees_in_department(id):
    res = []
    department = [d for d in ui.ui_controller.departments if d["id"] == id][0]
    for e_id in department["employees"]:
        res.append([e for e in ui.ui_controller.employees if e["id"] == e_id])
    res_str = ("\n".join(str(x) for x in res))
    return res_str

def input_name_department(new_dep):
    add_department(new_dep)
    return f"ADDED NEW DEPARTMENT {new_dep}"

def input_employee(empl_dict: dict):
    add_employee(empl_dict['name'], empl_dict['salary'])
    return f"ADDED NEW EMPLOYEE {empl_dict['name']}"

def input_id_tohire(hire_dict: dict):
    id_employee = hire_dict['id_employee']
    id_department = hire_dict['id_department']
    if not is_employee_in_department(id_employee, id_department):
        if is_id(id_department, departments) and is_id(id_employee, employees):
            hire_employee(id_employee, id_department)
            return "Сотрудник успешно нанят", f"HIRED EMPLOYEE ID {id_employee} IN DEPARTAMENT ID {id_department}"
        else:
            return "Такого(их) ID в базе не существует."
    else:
        return "Этот сотрудник уже работает в указанном отделе"

def input_for_transfer(move_dict: dict):
    id_employee = move_dict['id_employee']
    id_department = move_dict['id_department']
    if is_id(id_employee, employees):
        if is_id(id_department, departments):
            if not is_employee_in_department(id_employee, id_department):
                dep_cur = transfer_employee(id_employee, id_department)
                return f"Сотрудник успешно переведен в {dep_cur}", f"TRANSFERED EMPLOYEE ID {id_employee} TO DEPARTAMENT ID {id_department}"
            else:
                return "Сотрудника не перевести, он уже работает в этом отделе."
        else:
            return f"Такого ID в базе не существует."
    else:
        return f"Такого ID в базе не существует."

def input_for_dismiss(id_employee):
    # id_employee = input_check("Введите id сотрудника: ", 1)
    if is_id(id_employee, employees):
        lst = list((x["name"] for x in departments if id_employee in x["employees"]))
        # print("Сотрудник будет уволен из отдела", lst[0])
        dismiss_emloyee(id_employee)
        return "Сотрудник успешно уволен", f"EMPLOYEE ID {id_employee} DISMISSED"
    else:
        return f"Такого ID в базе не существует."

