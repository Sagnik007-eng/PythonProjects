import csv
temp_list=[]
temp1=[]
with open("weather_data.csv") as l:
    csv1 = csv.reader(l)
    for i in csv1:
        temp_list.append(i)


for i in range(1,len(temp_list)):
    temp1.append(int(temp_list[i][1]))

#print(temp1)
import pandas
df=pandas.read_csv("weather_data.csv")
#print(df)
#l=df["temp"].to_list()
"""s=0
for i in l:
    s=s+i
avg=s/len(l)
print(avg)"""
#print(df["temp"].max())
#print(df[df.temp==df["temp"].max()])
temp=df[df.day=="Monday"]["temp"]
print(temp * 9/5 +32)