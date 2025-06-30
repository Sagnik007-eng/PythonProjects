myList = ['Java', 'Data Science', 'Python', 'Machine Learning', 'Artificial Intelligence']

d={len(i):i for i in myList}

l=[len(i) for i in myList]  

for i,j in d.items():
    if i==max(l):
        print(j)