
#copying inactive members from a file to another file

with open('F:/Python/CurrentMem.txt','r') as currentmem:
    currentmemlist=currentmem.readlines()

with open('F:/Python/Exmem.txt','r') as exmem_read:
    exmem_read1=exmem_read.readlines()

emptylist=[]
for i in exmem_read1:
    emptylist.append(i.split(',')[0])

exmem=open('F:/Python/Exmem.txt','a')

for i in currentmemlist:
    if i.__contains__(',No'):
        if i.split(',')[0] not in emptylist:
            exmem.write(i)
exmem.close()
