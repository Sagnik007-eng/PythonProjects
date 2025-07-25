l='mamma mia mm'
l1=[i for i in l]
s1=set(l1)
d={}

for i in s1:
    c=0
    for j in l1:
        if i==j:
            c=c+1
    d[i]=c

print(d)
