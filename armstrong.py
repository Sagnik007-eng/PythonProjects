
def armstrong(s):
    l = []
    for i in str(s):
        l.append(int(i))
    sum = 0
    for i in l:
        sum = sum + i ** len(str(s))

    if sum == int(s):
        print(f'{s} is Armstrong')



for s in range(100,1700):
    armstrong(s)