from logg import log_find
def find_in(file: str, r: int, value: str) -> list:
    """
    Поиск по файлу данных
    стребуется указать путь/имя файла, столбец в котором ищем и собственно что ищем
    просто печатает строки содержащие найденое
    возвращает список списков )
    """
    data = []
    res = []
    with open(file, newline='', encoding="utf-8") as o_file:
        reader1 = o_file.readline().replace('\ufeff', '').replace('\r\n', '')   # убираю залоговок и окончание
        reader2 = o_file.readlines()
        print(reader1)
        count = 0             # счетчик
        for row in reader2:
            row = row.replace('\r\n', '')
            if row:
                res = row.split(';')
                # по наличию в строке без учета регистра
                if value.lower() in res[r].lower():
                    # if res[r].lower().startswith(value.lower()):  # по началу строки без учета регистра
                    print(row)
                    count += 1
                    data.append(row)
                else:
                    continue
            else:
                continue
        if not count:       # Если счетчик == 0 
            print('По запросу ничего не найдено!')
        log_find()
        # res = [x for x in data if value in ''.split(data)]
    return data


def find_last_id(file: str) -> int:
    """
    Поиск по файлу данных
    Возвращает максимальный id встреченный в столцбе 0
    """
    with open(file, newline='', encoding="utf-8") as o_file:
        reader1 = o_file.readline()
        reader2 = o_file.readlines()
        res = []
        data = []
        for row in reader2:
            row = row.replace('\r\n', '')
            if row:
                res = row.split(';')
                data.append(int(res[0]))
            else:
                continue
    return max(data)


# fil = 'Psih_palata/Personal.csv'
# fil = 'Psih_palata/Patients.csv'
# find_in(fil, 1, 'ар')     # name
# find_in(fil, 5, 's')      # sr size
# find_in(fil, 1, 'а')      # surname
# print(find_last_id(fil))