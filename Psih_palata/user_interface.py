
from show import show_data
from find   import find_in
from add    import add_new_worker, add_new_ward
from delete import delete_worker,delete_ward
from error  import check_in, get_mode
from change import menu_change_info_s, menu_change_info_p
from logg   import start_app, quit_app, next_step, show_data as log_show_data

from global_v  import file_personal, file_patients

def comm_menu():
    print(f'\nПсихиатрическая больница "Палата №6" \n')
    return check_in(input(f'1. Сотрудники\n'
                          f'2. Пациенты\n'
                           '0. Выход\n'),2)


def menu_find_personal():
    return check_in(input('\nКритерии поиска:\n'
                           '1. Фамилия\n'
                           '2. Должность\n'
                           '3. Парковочное место\n'
                           '0. Предыдущее меню\n'),3)


def menu_find_patient():
    return check_in(input('\nКритерии поиска:\n'
                           '1. Фамилия\n'
                           '2. Диагноз\n'
                           '3. Палата\n'
                           '0. Предыдущее меню\n'),3)


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
    while check_in(input('\n1. Показать всех сотрудников\n'
                          '2. Найти сотрудника\n'
                          '3. Обновить данные сотрудника\n'
                          '4. Добавить сотрудника\n'
                          '5. Удалить данные о сотруднике\n'
                          '0. Предыдущее меню\n'),5):
        match get_mode():
            case 1:
                next_step()
                show_data(file_personal)
                log_show_data()
            case 2:
                next_step()
                while menu_find_personal():
                    match get_mode():
                        case 1:
                            next_step()
                            find_in(file_personal, 2, surname_in())
                        case 2:
                            next_step()
                            find_in(file_personal, 3, special_in())
                        case 3:
                            next_step()
                            find_in(file_personal, 5, parking_in())
            case 3:
                next_step()
                menu_change_info_s()
            case 4:
                next_step()
                add_new_worker()
            case 5:
                next_step()
                delete_worker()



def patient_menu():
    while check_in(input('\n1. Показать всех пациентов\n'
                          '2. Найти пациента\n'
                          '3. Обновить данные пациента\n'
                          '4. Добавить пацента\n'
                          '5. Удалить данные о пациенте\n'
                          '0. Предыдущее меню\n'),5):
        match get_mode():
            case 1:
                next_step()
                show_data(file_patients)
                log_show_data()
            case 2:
                next_step()
                while menu_find_patient():
                    match get_mode():
                        case 1:
                            next_step()
                            find_in(file_patients, 2, surname_in())
                        case 2:
                            next_step()
                            find_in(file_patients, 3, diag_in())
                        case 3:
                            next_step()
                            find_in(file_patients, 4, room_in())
            case 3:
                next_step()
                menu_change_info_p()
            case 4:
                next_step()
                add_new_ward()
            case 5:
                next_step()
                delete_ward()


def welcome():
    start_app() 
    while comm_menu():
        match get_mode():
            case 1:
                next_step()
                personal_menu()
            case 2:
                next_step()
                patient_menu()
    quit_app()
