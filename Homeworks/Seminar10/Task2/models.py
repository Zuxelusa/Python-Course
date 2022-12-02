# departments = [
#     {"id": 10, "name": "accounting", "employees": [2, 1]},
#     {"id": 11, "name": "marketing", "employees": [3]}
# ]
#
# employees = [
#     {"id": 1, "fio": "ivan petrov", "salary": 40},
#     {"id": 2, "fio": "bob ivanov", "salary": 50},
#     {"id": 3, "fio": "jon don", "salary": 100}
# ]
import ui

employees = []
departments = []

def find_last_id(lst):
    return max([i["id"] for i in lst])


def is_id(element_id, dictionary):
    return element_id in [x["id"] for x in dictionary]


def is_employee_in_department(id_employee, id_department):
    if id_employee in [x["employees"] for x in departments if x["id"] == id_department][0]:
        return True
    else:
        return False

def add_department(name):
    print(departments)
    note_to_add = {"id": find_last_id(departments) + 1, "name": name, "employees": []}
    departments.append(note_to_add)

def add_employee(fio, salary):
    note_to_add = {"id": find_last_id(employees) + 1, "fio": fio, "salary": salary}
    employees.append(note_to_add)

def hire_employee(id_employee, id_department):
    department = [x for x in departments if id_department == x["id"]][0]
    departments.remove(department)
    department["employees"].append(id_employee)
    departments.append(department)

def dismiss_emloyee(id_employee):
    department = [x for x in departments if id_employee in x["employees"]][0]
    departments.remove(department)
    department["employees"].remove(id_employee)
    departments.append(department)

def transfer_employee(id_employee, id_department):
    # TODO: увольняем сотрудника из отдела
    dismiss_emloyee(id_employee)
    # TODO: добавляем сотрудника в новый отдел
    department = [x for x in departments if id_department == x["id"]][0]
    departments.remove(department)
    department["employees"].append(id_employee)
    departments.append(department)
    return department["name"]
