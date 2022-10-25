from datetime import datetime

def log_error():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('Enter error at {}\n'.format(time_calc))


def log_start():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('Start work with app at {}\n'.format(time_calc))

def log_quit():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('End of work with app at {}\n'.format(time_calc))

def log_next():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User make new choice at {}\n'.format(time_calc))

def log_show():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User check data at {}\n'.format(time_calc))

def log_fill():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User add data at {}\n'.format(time_calc))

def log_find():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User find wanted person at {}\n'.format(time_calc))

def log_refresh():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User refreshed data at {}\n'.format(time_calc))

def log_delete():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User delete person data at {}\n'.format(time_calc))

def log_add(fail: str, id: int):
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write(f'User add person data at {fail} id {id}\n'.format(time_calc))