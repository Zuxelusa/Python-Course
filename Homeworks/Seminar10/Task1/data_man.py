import os.path
import pickle


DB_PATH = "data_files\\"


def save_data(f_name, d):
    with open(DB_PATH + str(f_name) + ".pickle", "wb") as f:
        pickle.dump(d, f)


def read_data_init(f_name, data):
    if not os.path.isfile(str(f_name) + ".pickle"):
        d = data
        save_data(str(f_name), d)


def read_data(f_name):
    with open(DB_PATH + str(f_name) + ".pickle", "rb") as f:
        d = pickle.load(f)
    return d
