s='ystsb njiopolpafgei umbrellaur great'
l=['a','e','i','o','u']
l1=[]
for i in s:
    if i in l:
        l1.append(i)

i=0
o=0
a=0
e=0
print(l1)
for j in l1:
    if j=='i':
        i=i+1
    elif j=='o':
        o=o+1
    elif j=='a':
        a=a+1
    elif j=='e':
        e=e+1
print(f'thr r {i} i,{o} o,{a} a,{e} e')

d={}
d['i']=0
d['o']=0
d['a']=0
d['e']=0
for j in l1:
    if j=='i':
        d['i']=d['i']+1
    elif j=='o':
        d['o'] = d['o'] + 1
    elif j == 'a':
        d['a'] = d['a'] + 1
    elif j == 'e':
        d['e'] = d['e'] + 1

print(d)