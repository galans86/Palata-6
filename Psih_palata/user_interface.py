#from Psih_palata.delete import delete_worker
from show import show_data
# import logg
from find import find_in
from add import add_new_worker, add_new_ward
from delete import delete_worker
from delete import delete_ward
from refresh import read_data
from refresh import change_info_file
# import delete
from error import check_in1, check_in2, check_in3, get_mode
from error import file_personal, file_patients
from change import menu_change_info_s, menu_change_info_p


def comm_menu():
    print(f'\nПсихиатрическая больница "Палата №6" \n')
    return check_in1(input(f'1. Сотрудники\n'
                           f'2. Пациенты\n'
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


def personal_menu():
    while check_in2(input('\n1. Показать всех сотрудников\n'
                          '2. Найти сотрудника\n'
                          '3. Обновить данные сотрудника\n'
                          '4. Добавить сотрудника\n'
                          '5. Удалить данные о сотруднике\n'
                          '0. Предыдущее меню\n')):
        match get_mode():
            case 1:
                show_data(file_personal)
            case 2:
                while menu_find_personal():
                    match get_mode():
                        case 1:
                            find_in(file_personal, 2, surname_in())
                        case 2:
                            find_in(file_personal, 3, special_in())
                        case 3:
                            find_in(file_personal, 5, parking_in())
            case 3:
                menu_change_info_s()
            case 4:
                add_new_worker()
            case 5:
                delete_worker()



def patient_menu():
    while check_in2(input('\n1. Показать всех пациентов\n'
                          '2. Найти пациента\n'
                          '3. Обновить данные пациента\n'
                          '4. Добавить пацента\n'
                          '5. Удалить данные о пациенте\n'
                          '0. Предыдущее меню\n')):
        match get_mode():
            case 1:
                show_data(file_patients)
            case 2:
                while menu_find_patient():
                    match get_mode():
                        case 1:
                            find_in(file_patients, 2, surname_in())
                        case 2:
                            find_in(file_patients, 3, diag_in())
                        case 3:
                            find_in(file_patients, 4, room_in())
            case 3:
                menu_change_info_p()
            case 4:
                add_new_ward()
            case 5:
                delete_ward()


def welcome():
    while comm_menu():
        match get_mode():
            case 1:
                personal_menu()
            case 2:
                patient_menu()


welcome()
