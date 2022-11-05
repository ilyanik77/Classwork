
import csv
#import os -чтобы удалить файл

# чтение csv
with open('file.csv', encoding = "utf_8") as csvfile:
    reader = csv.reader(csvfile, delimiter = ";")
    #title = next(reader) -чтобы не счтывалась строка заголовка
    #sp = [] -сохраняем список,чтобы доступ к файлу был многоразовым
    for row in reader:
        #sp.append(row)
        print(row)
        
        
# чтение csv в словарь
with open('file.csv', encoding = "utf_8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ";")
    expensive = sorted(reader, key = lambda x: int(x['price']), reverse = True) # сортировка по цене
    
for record in expensive:
    print(record)  
    
   
# os.remove('file.csv') -удаление файла