import requests
import json
import csv
response=requests.get('https://jsonplaceholder.typicode.com/users')
obj1=json.loads(response.text)
#print(obj1)

l=[]

for i in obj1:
    l.append((i['name'],i['address']['city'],(i['address']['geo']['lat'],i['address']['geo']['lng']),i['company']['name']))


with open(r'C:\Users\SagnikBhattacharya\Desktop\files\nestedfolder\emp.csv','a') as f:
    writer=csv.writer(f,lineterminator='\n')
    for i in l:
        writer.writerow(i)
