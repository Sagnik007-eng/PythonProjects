with open(r'C:\Users\SagnikBhattacharya\Desktop\files\banking.txt') as f:
    l=f.readlines()
#print(l)
# s='\n'.join(l)
# print(s)
clean_list=[]
for i in l:
    clean_list.append(i.strip())
#print(clean_list)
sum1=0
for i in clean_list:
    if i.split(':')[0]=='D':
        sum1=sum1+int(i.split(':')[1])
    elif i.split(':')[0]=='W':
        sum1 = sum1 - int(i.split(':')[1])
print(sum1)