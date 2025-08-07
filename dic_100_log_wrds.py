#In a file words are arranged in following way. Need to write the following
# into a dictionary & need to read 100 longest wrds in the file

# A
# AMD
# AOL
# AWS
# Aachen
# Aaliyah
# Aaron
# Abbas
# Abbasid
# Abbott

with open(r'C:\Users\SagnikBhattacharya\Desktop\files\american-english.txt') as f:
    l1=f.readlines()
dic1={}
for i in l1:
    dic1[i.strip()]=len(i.strip())
l1=[i for i in dic1.values()]
l2=sorted(l1,reverse=True)
l2=l2[:100]
#print(l2)
d_100={}
for i in dic1:
    if dic1[i] in l2:
        d_100[i]=len(i)
print(d_100)

