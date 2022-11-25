memory = 0

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

OPERATIONS = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def calculate(a: int, b: int, menu_item):
    return OPERATIONS[menu_item](a, b)