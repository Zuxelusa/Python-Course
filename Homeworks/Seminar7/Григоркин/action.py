def read_base(file):
    print('Чтение')
    with open(file, 'r', encoding='utf-8') as text:
        resultData = list()
        for line in text.readlines():
            resultData.append(tuple(line.split('\n')[0].split(';')))
    # print(resultData)
    return resultData

def read_base_(file):
    print('Чтение')
    with open(file, 'r', encoding='utf-8') as text:
        last_id=int(text.readline().split('\n')[0])
        resultData = list()
        dict_contact={}
        dict_phone={}
        for line in text.readlines():
            list_record=line.split('\n')[0].split(';')
            dict_contact[int(list_record[0])]=list_record[1]
            dict_phone[int(list_record[0])]=list_record[2]
        resultData.append(tuple([dict_contact,dict_phone]))
    return resultData, last_id

print (read_base_("phone.txt"))
# ids, fio, phones = zip(*read_base("phone.txt"))
# ids, fio, phones = zip(*read_base_("phone.txt"))
# print
# print(ids)
# print(fio)
# print(phones)


def save_base(file,base):
    print('Запись')
    with open(file, 'w', encoding='utf-8') as text:
        for line in range(len(base)):
            str_phone=''
            for num in range(len(base[line])-2):
                str_phone+=';'+base[line][num+2]
            text.write(base[line][0]+';'+base[line][1]+str_phone+'\n')

def find_contact():
    print('Поиск')
    return

def edit_contact():
    print('Редактирование')
    return

def new_contact():
    print('Новый контакт')
    return

def del_contact():
    print('Удаление')
    return

def import_contacts():
    print('Импорт')
    return

def export_contacts():
    print('Экспорт')
    return

OPERATIONS = {
   "1": find_contact,
   "2": edit_contact,
   "3": new_contact,
   "4": del_contact,
   "5": import_contacts,
   "6": export_contacts
}


def choice(op):
    OPERATIONS[op]()

