import csv

def find_in(file: str, r: int, value : str) -> list:
    """
    Поиск по файлу данных
    стребуется указать путь\имя файла, столбец в котором ищем и собственно что ищем
    возвращает список списков )
    или просто печатает?
    """
    data = []
    res = []
    with open(file, newline='', encoding="utf-8") as File:  
        reader = csv.reader(File)
        for row in reader:
            res = row[0].split(';')
            if value in res[r]:
                print(row)
                data.append(row)
            else:
                continue
        # res = [x for x in data if value in ''.split(data)]
    return data

# fil = 'Psih_palata\Patiens
# print(find)
