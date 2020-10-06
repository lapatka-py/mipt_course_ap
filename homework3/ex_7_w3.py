import csv

with open('table.csv', 'r+') as file:
    csv_reader = csv.reader(file)
    data = []
    for i, row in enumerate(csv_reader):
        item = list(map(str, row[0].split(';')))
        if item != []:
            data.append(item)
    data[0].append('my_col')
    for i in range(1, len(data)):
        data[i].append('True')
    writer = csv.writer(file)
    writer.writerows(data)