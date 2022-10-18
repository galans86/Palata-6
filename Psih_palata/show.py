def show_data(file):
    with open(file, newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)