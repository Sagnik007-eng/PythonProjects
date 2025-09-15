l=['apple','orange','apple','banana','mango','papaya','papaya','mango','apple','orange']


d={}

for i in l:
    count = 0
    for j in l:
        if i==j:
            count=count+1
        d[i]=count


print(d)