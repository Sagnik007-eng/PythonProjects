import csv
people = [['Dan', 34, 'Bucharest'],['Andrei',21, 'London'],['Maria', 45, 'Paris']]
csv.register_dialect('colon', delimiter=':', quoting=csv.QUOTE_NONE, lineterminator='\n')
with open(r'C:\Users\SagnikBhattacharya\Desktop\files\nestedfolder\people2.csv','a') as f:
    writer=csv.writer(f,dialect='colon')
    for i in people:
        writer.writerow(i)

with open(r'C:\Users\SagnikBhattacharya\Desktop\files\nestedfolder\people2.csv','r') as f:
    reader=csv.reader(f,dialect='colon')
    for i in reader:
        print(i)