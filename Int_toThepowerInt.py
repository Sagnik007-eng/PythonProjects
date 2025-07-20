num1=int(input('Enter int'))
num2=int(input('Enter int'))
big,small=0,0
i=0
if num1>num2:
    big=num1;small=num2
else:
    small = num1;big = num2

print(f'small is {small} big is {big}')

while(True):

    if small**i==big:
        print(f'{small}  to the power {i} eq to {big}')
        break
    elif small**i>big:
        print(f'{small}  to the power {i} is gt than {big}')
        break
    elif small==1:
        print(f'small is {small}.its power of anything is always 1')
        break

    i=i+1