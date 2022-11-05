import csv

# 1-показать меню
def csv_data_open():      
    with open('csv_data.csv', encoding= 'utf_8') as file:
        file_csv = csv.reader(file, delimiter= ';')
        res = list(file_csv)
    return res

# 2-добавить запись
def add_info(list):
    with open('csv_data.csv', 'a', encoding= 'utf_8', newline='') as f:
        writer = csv.writer(f, delimiter= ';')
        writer.writerow(list) 

# list = ['Мама', 'Папа', '25544']
# add_info(list)

# 3-удалить запись
def del_info(index):
    list_csv = csv_data_open()
    del list_csv[index]
    with open('csv_data.csv', 'w', encoding= 'utf_8', newline= '') as file:
        writer = csv.writer(file, delimiter= ';')
        for row in list_csv:
            writer.writerow(row)
           

# 4-обновление информации
def update_info(index, tel):
    list_csv = csv_data_open()
    list_csv[index][3] =  tel
    with open('csv_data.csv', 'a', encoding= 'utf_8', newline= '') as file:
        writer = csv.writer(file, delimiter= ';')
        for row in list_csv:
            writer.writerow(row)