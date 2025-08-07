#In a file words are arranged in following way. Need to find the alphabet count

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

import time
sec1=time.time()
with open(r'C:\Users\SagnikBhattacharya\Desktop\files\american-english.txt') as f:
    s=f.readlines()
l1=[]
for i in s:
    l1.append(i.strip())


s1=''.join(l1)
#print(s1)
l=[]
for i in s1:
   l.append(i)
#print(l)
d={}
for i in l:
       d[i]=l.count(i)
print(d)
sec2=time.time()
print(f'{sec2-sec1} is total time taken')

#O/P should be in following format
#{'A': 755, 'M': 923, 'D': 439, 'O': 216, 'L': 487, 'W': 279, 'S': 864, 'a': 46143, 'c': 22849, 'h': 13605, 'e': 67681, 'n': 42357