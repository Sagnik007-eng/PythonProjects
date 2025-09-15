def f(n):
    for i in range(1,n):
        print(f'{i}',end=' ')
        if i%10==0:
            print('\n')


d={'Jan':32,'Feb':29,'Mar':32}

for i in d:
    print('\n')
    print(i)
    f(d[i])