import csv

start = 900

newcsv  = []

with open('50_percent_cheaters.csv', 'rb') as csvfile:
    experiment50 = csv.DictReader(csvfile)
    for row in experiment50:
        row['Run'] = int(row['Run']) - start
        newcsv.append(row)

with open('changed.csv', 'wb') as newfile:
    fieldnames = ["Run","Time","Status","Solver","Gas","Verifiers"]
    writer = csv.DictWriter(newfile,fieldnames)
    writer.writerows(newcsv)
