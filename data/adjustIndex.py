import csv

start = 690

newcsv  = []

with open('70_percent_cheaters2.csv', 'rb') as csvfile:
    experiment50 = csv.DictReader(csvfile)
    for row in experiment50:
        row['Run'] = int(row['Run']) + start
        newcsv.append(row)

with open('changed.csv', 'wb') as newfile:
    fieldnames = ["Run","Time","Status","Solver","Gas","Verifiers"]
    writer = csv.DictWriter(newfile,fieldnames)
    writer.writerows(newcsv)
