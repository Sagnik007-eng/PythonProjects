#Write a Program to combine two different dictionaries.
# While combining, if you find the same keys,
# you can add the values of these same keys. Output the new dictionary


d1={'One':1,'Two':2,'Three':3,'Six':6}
d2={'Four':4,'Five':5,'Three':3,'Six':6}
d3={}

l1=[i for i in d1.keys()]
l2=[i for i in d2.keys()]


comon_keys=[i for i in l1 for j in l2 if i==j]
for i in comon_keys:
    d3[i]=d1[i]+d2[i]
for i in comon_keys:
    d1.pop(i)
    d2.pop(i)

for i in d1.keys():
    d3[i]=d1[i]

for i in d2.keys():
    d3[i]=d2[i]

print(d3)