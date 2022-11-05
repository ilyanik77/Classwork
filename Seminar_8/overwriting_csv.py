import csv

with open('file.csv', encoding= 'utf_8') as csvfile, open('file2.csv', 'w', encoding= 'utf_8', newline= '') as f:
    reader = csv.reader(csvfile, delimiter= ';')
    writer = csv.writer(f, delimiter= ';')
    for row in reader:
        writer.writerow(row)