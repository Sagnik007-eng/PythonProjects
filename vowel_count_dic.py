st='abcdefghihjkeoi'
v='aeiou'
# d={}
# for i in v:
#    d[i]=st.count(i)
d1={}
d={i:st.lower().count(i) for i in v}
for i in d:
    if d[i]!=0:
        d1[i]=d[i]
print(d1)
