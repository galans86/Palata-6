from datetime import datetime

def error_enter():
    time_calc = datetime.now().strftime('%H:%M')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('Enter error at {}\n'.format(time_calc))


def start_app():
    time_calc = datetime.now().strftime('%H:%M')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('Start work with app at {}\n'.format(time_calc))

def quit_app():
    time_calc = datetime.now().strftime('%H:%M')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('End of work with app at {}\n'.format(time_calc))

def next_step():
    time_calc = datetime.now().strftime('%H:%M')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User make new choice at {}\n'.format(time_calc))

def show_data():
    time_calc = datetime.now().strftime('%H:%M')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User check data at {}\n'.format(time_calc))

def fill():
    time_calc = datetime.now().strftime('%H:%M')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User add data at {}\n'.format(time_calc))

def find():
    time_calc = datetime.now().strftime('%H:%M')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User find wanted person at {}\n'.format(time_calc))

def refresh():
    time_calc = datetime.now().strftime('%H:%M')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User refreshed data at {}\n'.format(time_calc))

def delete():
    time_calc = datetime.now().strftime('%H:%M')
    with open('Psih_palata/log.csv', 'a') as log_file:
        log_file.write('User delete person data at {}\n'.format(time_calc))