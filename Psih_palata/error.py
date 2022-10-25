
mode = 0

def get_mode():
    return mode


def check_in1(in_mode):
    global mode
    mode = int(in_mode) if in_mode in ['1', '2'] else 0
    return mode


def check_in2(in_mode):
    global mode
    mode = int(in_mode) if in_mode in ['1', '2', '3', '4', '5'] else 0
    return mode


def check_in3(in_mode):
    global mode
    mode = int(in_mode) if in_mode in ['1', '2', '3'] else 0
    return mode


def exception_name(message):
    for i in "!@#$%^&/*?<>1234567890'\"":
        if message.find(i) >= 0:
            return False
    else:
        return True


def exception_menu_item(value):
    if value.isdigit() and (int(value) in [1, 2, 3, 4, 5, 6, 7]):
        return True
    else:
        return False


def exception_id(value):
    value = value.replace(" ", '')
    if value.isdigit() and len(value) < 4:
        return True
    else:
        return False
