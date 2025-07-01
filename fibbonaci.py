l=[1,1]
while True:
    if l[-1]>100:
        break
    s=l[-1]+l[-2]
    l.append(s)

print(l)