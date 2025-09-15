def matrix_addition(l1,l2):
    l = []  # Empty list to catch the element causing inequality
    if len(l1) == len(l2):
        for i in range(0, len(l1)):
            if len(l1[i]) == len(l2[i]):
                continue
            else:
                print(f'{i}th element lenth is not same so not possible to add')
                l.append(i)
                break

    else:
        print('Length is not equal so addition not possible')

    if len(l) == 0:
        print(f'Addition possible. Its a {len(l1)}*{len(l1[0])} matrix')
        l_iner=[];l_outr=[]
        for i in range(0,len(l1[0])):
            l_iner.append(0)
        for i in range(0,len(l1)):
            l_outr.append(l_iner)
        for i in range(0,len(l1)):
            for j in range(0,len(l1[0])):
                l_outr[i][j]=l1[i][j]+l2[i][j]
        print(l_outr)
    else:
        print('Addition not possible')

matrix_addition([[1,1,1],[1,1,1],[1,1,1],[1,1,1]],[[1,1,1],[1,1,1],[1,1,1],[1,1,1]])