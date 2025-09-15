"""
Name,Active
XYZ,Yes
TSB,No

We need to remove records with No
"""
with open('F:/Python/file.txt','r') as currentmem:
    currentmemlist=currentmem.readlines()
print("before update")
print(currentmemlist)


empty_list=[]
for i in currentmemlist:
    if i.split(',')[1]!='No\n':
        empty_list.append(i)

with open('F:/Python/file.txt','w') as f:
    for i in empty_list:
        f.write(i)
with open('F:/Python/file.txt','r') as f:
    l=f.readlines()

print("After copy  no 'no' ")
print(l)