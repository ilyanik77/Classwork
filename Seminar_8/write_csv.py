
import csv

# запись csv      
with open('file.csv', 'a', encoding='utf_8', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    row = ['колбаса', 500, 'Микоян']
    row1 = ['Йогурт', 34,'Данон']
    writer.writerow(row)
    writer.writerow(row1)
    
    
# запись словаря в файл csv
data = [{
    'lastname': 'Иванов',
    'firstname': 'Петр',
    'class_number': 9,
    'class_letter': 'A'
}, {
    'lastname': 'Кузнецов',
    'firstname': 'Алексей',
    'class_number': 9,
    'class_letter': 'B'
}, {
    'lastname': 'Меньшова',
    'firstname': 'Алиса',
    'class_number': 9,
    'class_letter': 'A'
}]

with open('dictwriter.csv', 'w', encoding= 'utf_8', newline= '') as f:
    writer = csv.DictWriter(f, fieldnames = list(data[0].keys()), delimiter = ';')
    writer.writeheader()
    for d in data:
        writer.writerow(d) 