import csv
people = [['Dan', 34, 'Bucharest'],['Andrei',21, 'London'],['Maria', 45, 'Paris']]

with open(r'C:\Users\SagnikBhattacharya\Desktop\files\nestedfolder\people1.csv','a') as f:
    writer=csv.writer(f,lineterminator='\n')
    for i in people:
        writer.writerow(i)



with open(r'C:\Users\SagnikBhattacharya\Desktop\files\nestedfolder\people1.csv','r') as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)