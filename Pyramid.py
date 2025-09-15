spacecount=0
for i in range(10,0,-2):
    print(((spacecount//2) * ' ')+(i*'*')+((spacecount//2) * ' '))
    spacecount=spacecount+2
    if i==2:
        print(((spacecount // 2) * ' ') + ('*') + ((spacecount // 2) * ' '))
        break