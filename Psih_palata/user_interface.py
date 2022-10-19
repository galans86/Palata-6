import show
# import logg
# import find
# import add
# import delete


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

def com_menu():
    print(f'\n{chr(127973)} Психиатрическая больница "Палата №6 {chr(128719)} " \n')
    return check_in1(input(f'1. Сотрудники {chr(128100)}\n'
                           f'2. Пациенты {chr(128581)}\n'
                           '0. Выход\n'))


def menu_find_personal():
    return check_in3(input('\nКритерии поиска:\n'
                           '1. ФИО\n'
                           '2. Должность\n'
                           '3. Кабинет\n'  # возможно уже лишнее
                           '0. Предыдущее меню\n'))

def menu_find_patient():
    return check_in3(input('\nКритерии поиска:\n'
                           '1. ФИО\n'
                           '2. Диагноз\n'
                           '3. Палата\n'
                           '0. Предыдущее меню\n'))


def personal_menu():
    while check_in2(input('\n1. Показать всех сотрудников\n'
                          '2. Найти сотрудника\n'
                          '3. Обновить данные сотрудника\n'
                          '4. Добавить сотрудника\n'
                          '5. Удалить данные о сотруднике\n'
                          '0. Предыдущее меню\n')):
        match get_mode():
            case 1:
                show('Personal.csv')
            case 2:
                while menu_find_personal():
                    match get_mode():
                        case 1:
                            print('find by fio in work\n')
                        case 2:
                            print('find by spec in work\n')
                        case 3:
                            print('find by room in work\n')
            case 3:
                print('refresh in work\n')
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
                show('Patients.csv')
            case 2:
                while menu_find_patient():
                    match get_mode():
                        case 1:
                            print('find by fio in work')
                        case 2:
                            print('find by diag in work')
                        case 3:
                            print('find by room in work')
            case 3:
                print('refresh in work')
            case 4:
                print('add in work')
            case 5:
                print('delete in work')


def welcome():
    while com_menu():
        match get_mode():
            case 1:
                personal_menu()
            case 2:
                patient_menu()


