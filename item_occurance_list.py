l=[1,2,3,1,3,3,4,2]
d={}
for i in l:
    print(f'{i} is present {l.count(i)} times')
    d[i]=l.count(i)
print(d)
