prime=[]
composite=[]
l=[i for i in range(2,50)]
for i in l:
    for j in range(2,i):
        #print(f'{i}%{j} is {i%j}')
        if i%j==0:
            #composite.append(i)
            break

    else:
        prime.append(i)





print(composite)
print(prime)