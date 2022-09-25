import csv

fileName = input()  # vacancies.csv
rightList = []

with open(fileName, encoding='utf_8_sig') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        if row:
            if not row.__contains__('') and len(row) > 1:
                rightList.append(row)

print(list(rightList))
