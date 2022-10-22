import show
# import logg
from find import find_in
# import add
# import delete
from refresh import read_data
from refresh import change_info_file

mode = 0

def get_mode():
    return mode

def check_in1(in_mode):
    global mode
    mode = int(in_mode) if in_mode in ['1', '2'] else 0
    return mode


def check_in2(in_mode):
    global mode
    mode = int(in_mode) if in_mode in [
        '1', '2', '3', '4', '5'] else 0
    return mode


def check_in3(in_mode):
    global mode
    mode = int(in_mode) if in_mode in ['1', '2', '3'] else 0
    return mode

def comm_menu():
    print(f'\n{chr(127973)} Психиатрическая больница "Палата №6 {chr(128719)} " \n')
    return check_in1(input(f'1. Сотрудники {chr(128100)}\n'
                           f'2. Пациенты {chr(128581)}\n'
                            '0. Выход\n'))


def menu_find_personal():
    return check_in3(input('\nКритерии поиска:\n'
                           '1. Фамилия\n'
                           '2. Должность\n'
                           '3. Парковочное место\n'  
                           '0. Предыдущее меню\n'))

def menu_find_patient():
    return check_in3(input('\nКритерии поиска:\n'
                           '1. Фамилия\n'
                           '2. Диагноз\n'
                           '3. Палата\n'
                           '0. Предыдущее меню\n'))

def surname_in():
    return input('Введите фамилию: ')

def special_in():
    return input('Введите должность: ')

def parking_in():
    return input('Введите номер парковочного места: ')

def diag_in():
    return input('Введите диагноз: ')

def room_in():
    return input('Введите номер палаты: ')

def get_name(message):
    while True:
        value = input(message)
        if exception_name(value):
            return value
        else:
            print("\n", "-"*20, "Invalid name, repeat input", "-"*20)


def exception_name(message):   # доделать
        return True

def to_continee(messege):
    input(messege)


def exception_menu_item(value): # доделать
    value=value
    return True


def get_value(message):
    while True:
        value = input(message)
        if exception_menu_item(value):
            return int(value)
        else:
            print("\n", "-"*20, "Invalid number, repeat input", "-"*20)

def menu_change_info_p():
    id = get_id("Input id patient: ")
    data = read_data('Patients.csv')
    if data[0] == 0:
        return ""
    for i in data:
        i_temp = i.replace("\n", '').split(';')
        if i_temp[0] == id:
            print(f"пациент найден - {i_temp[1]} {i_temp[2]}, диагноз  - {i_temp[3]}, палата - {i_temp[4]}")
            id, last_name, first_name, diagnosis, chamber, size_cp , status = i_temp
            break
    else:
        return print("The id is missing!")
    print()
    print( "1 last_name", "2 first_name", "3 diagnosis", "4 chamber",
          "5 size_cp", "6 status", "7 return to the  previous menu",  sep="\n")
    num = get_value("\n Select item for change: ")
    match num:
        case 1:
            last_name = get_name('Input last name: ')
            to_continee("To continue peress Enter")
        case 2:
            first_name = get_name('Input first name: ')
            to_continee("To continue peress Enter")
        case 3:
            diagnosis = get_name('Input diagnosis: ')
            to_continee("To continue peress Enter")
        case 4:
            chamber = get_value('Input chamber: ')
            to_continee("To continue peress Enter")
        case 5:
            size_cp = get_name('Input size_cp: ')
            to_continee("To continue peress Enter")
        case 6:
            status = get_name('Input  status: ')
            to_continee("To continue peress Enter")
        case 7:
            menu_change_info_p()
    change_info_file('Patients.csv', id, last_name, first_name, diagnosis, chamber, size_cp , status)

# id;Имя;Фамилия;Должность;Телефон;Парковочное место;Подопечный

def menu_change_info_s():
    id = get_id("Input id employee: ")
    data = read_data('Personal.csv')
    if data[0] == 0:
        return print('error')
    for i in data:
        i_temp = i.replace("\n", '').split(';')
        if i_temp[0] == id:
            print(f"пациент найден - {i_temp[1]} {i_temp[2]}, диагноз  - {i_temp[3]}, палата - {i_temp[4]}")
            id, last_name, first_name, specialization, telethone, place , patient = i_temp
            break
    else:
        return print("The id is missing!")
    print()
    print( "1 last_name", "2 first_name", "3 specialization", "4 telethone",
          "5 place", "6 patient ", "7 return to the  previous menu",  sep="\n")
    num = get_value("\n Select item for change: ")
    match num:
        case 1:
            last_name = get_name('Input last name: ')
            to_continee("To continue peress Enter")
        case 2:
            first_name = get_name('Input first name: ')
            to_continee("To continue peress Enter")
        case 3:
            specialization = get_name('Input specialization: ')
            to_continee("To continue peress Enter")
        case 4:
            telethone = get_value('Input telethone: ')
            to_continee("To continue peress Enter")
        case 5:
            place = get_name('Input parking place number: ')
            to_continee("To continue peress Enter")
        case 6:
            patient = get_name('Input  patient: ')
            to_continee("To continue peress Enter")
        case 7:
            menu_change_info_s()

    change_info_file('Personal.csv', id, last_name, first_name, specialization, telethone, place , patient)





def get_id(message):
    while True:
        value = input(message)
        if exception_id(value):
            return value
        else:
            print("\n", "-"*20, "Invalid id, repeat input", "-"*20)


def  exception_id(value):    # проверка id доделать
    return True


def personal_menu():
    while check_in2(input('\n1. Показать всех сотрудников\n'
                          '2. Найти сотрудника\n'
                          '3. Обновить данные сотрудника\n'
                          '4. Добавить сотрудника\n'
                          '5. Удалить данные о сотруднике\n'
                          '0. Предыдущее меню\n')):
        match get_mode():
            case 1:
                show.show_data('Psih_palata/Personal.csv')
            case 2:
                while menu_find_personal():
                    match get_mode():
                        case 1:
                            print(find_in('Psih_palata/Personal.csv',3,surname_in()))
                        case 2:
                            print(find_in('Psih_palata/Personal.csv',4,special_in()))
                        case 3:
                            print(find_in('Psih_palata/Personal.csv',6,parking_in()))
            case 3:
                menu_change_info_s()
            case 4:
                print('add in work\n')
            case 5:
                print('delete in work\n')


def patient_menu():
    while check_in2(input('\n1. Показать всех пациентов\n'
                          '2. Найти пациента\n'
                          '3. Обновить данные пациента\n'
                          '4. Добавить пацента\n'
                          '5. Удалить данные о пациенте\n'
                          '0. Предыдущее меню\n')):
        match get_mode():
            case 1:
                show.show_data('Psih_palata/Patients.csv')
            case 2:
                while menu_find_patient():
                    match get_mode():
                        case 1:
                            print(find_in('Psih_palata/Patients.csv',3,surname_in()))
                        case 2:
                            print(find_in('Psih_palata/Patients.csv',4,diag_in()))
                        case 3:
                            print(find_in('Psih_palata/Patients.csv',5,room_in()))
            case 3:
                menu_change_info_p()
                to_continee("To continue peress Enter")
            case 4:
                print('add in work')
            case 5:
                print('delete in work')


def welcome():
    while comm_menu():
        match get_mode():
            case 1:
                personal_menu()
            case 2:
                patient_menu()

welcome()