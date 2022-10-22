from os import path

# id;Имя;Фамилия;"Диагноз";Палата;РазмерСР;Статус
# 0;Арсений;Беляев;буйный;206;S;Болеет

def change_info_file(file_name, id: str, last_name, first_name, diagnosis, chamber : str, size_cp , status):
    new_str = '{0};{1};{2};{3};{4};{5};{6}\n'.format(id, last_name, first_name, diagnosis, chamber, size_cp, status)
    if path.isfile(file_name):
        with open(file_name, 'r', encoding="utf-8") as file1:
            data = file1.readlines()
            for i in range(len(data)):
                lst = data[i].replace("\n", '').split(';')
                if lst[0] == id:
                    data[i] = new_str
                    break
        with open(file_name, 'w', encoding="utf-8") as file2:   
            file2.writelines(data)    
        print("Data added to",  file_name)
    else:
        print("File not found, write the data to a file")
        return 0

# change_info_file('Patients.csv', '1', 'Ирина2','Боярчукова','представлет себя Золушкой','110','S','Болеет')


def read_data(file_name):
    if path.isfile(file_name):
        with open(file_name, 'r', encoding="utf-8") as file1:
            data = file1.readlines()
        return data
    else:
        print("File not found, write the data to a file", file_name)
        return [0]
