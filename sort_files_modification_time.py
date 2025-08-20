import os
l=[]
"""
This code will explore the files in a folder convert into a list and sort in a asc order 
of modification time
"""
for i in os.listdir(r'C:\Users\SagnikBhattacharya\Desktop\files'):
    l.append((i, os.path.getmtime(f'C:/Users/SagnikBhattacharya/Desktop/files/{i}')))

l1=sorted(l,key=lambda x:x[1])
print(l1)