import csv
from refresh import read_data

def delete_worker():
    
    del_id = int(input())
    result = []
    data = read_data('Psih_palata/Personal.csv')
    data.pop(del_id)
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        result.append(row)
   
    print('Данные о сотруднике удалены')
    print(data)
    print(result)
#    writer = csv.writer(data, delimiter=',',quotechar=';', quoting=csv.QUOTE_MINIMAL)
#    for row in writer:
#            writer.writerow(result(zip(row)))
    return result


def delete_ward():
    del2_id = int(input())
    result2 = []
    data2 = read_data('Psih_palata/Patients.csv')
    data2.pop(del2_id)
    reader2 = csv.reader(data2, delimiter=',')
    for row in reader2:
        result2.append(row)
   
    print('Данные о пациенте удалены')
    print(data2)
    print(result2)

    return result2

