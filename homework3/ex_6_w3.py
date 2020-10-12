import csv

with open('table(1).csv', 'r') as file1:
    csv_reader = csv.reader(file1)
    data = []
    for i, row in enumerate(csv_reader):
        item = list(map(str, row[0].split(';')))
        if item != []:
            data.append(item)
        data.insert(len(data)//2, [200 for _ in range(len(data[0]))])

with open('middle_row.csv', 'w') as file2:
    writer = csv.writer(file2)
    writer.writerows(data)