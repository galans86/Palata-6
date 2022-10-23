import csv

def find_in(file: str, r: int, value : str) -> list:
    """
    Поиск по файлу данных
    стребуется указать путь/имя файла, столбец в котором ищем и собственно что ищем
    возвращает список списков )
    или просто печатает?
    """
    data = []
    res = []
    with open(file, newline='', encoding="utf-8") as File:  
        reader = csv.reader(File)
        for row in reader:
            res = row[0].split(';')
            if value.lower() in res[r].lower():      # по наличию в строке без учета регистра
            # if res[r].lower().startswith(value.lower()):  # по началу строки без учета регистра
                print(row)
                data.append(row)
            else:
                continue
        # res = [x for x in data if value in ''.split(data)]
    return data

# fil = 'Psih_palata/Patients.csv'
# find_in(fil, 1, 'ар')     # name
# find_in(fil, 5, 's')      # sr size
# find_in(fil, 2, 'а')      # surname