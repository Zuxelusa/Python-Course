
from models import *
import json

departments = []
employees = []

def read_data():
    read_json("employee", employees)
    read_json("department", departments)

PATH = "..\\"

def save_data():
    save_json("employee", employees)
    save_json("department", departments)

def save_json(name, my_dict):
    data = {}
    data[name] = []
    for i in my_dict:
        data[name].append(i)
    with open(PATH + name + ".json", "w") as f:
        json.dump(data, f)

def read_json(name, my_dict):
    with open(PATH + name + ".json", "r", encoding="utf-8") as f:
        data = json.load(f)
        my_dict.clear()
        for i in data[name]:
            my_dict.append(i)
    return my_dict

