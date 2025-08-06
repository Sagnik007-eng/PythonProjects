#The equilibrium index of an array is an index such that the sum of
# all elements at lower indexes equals the sum of all elements at higher indexes.


#eq_fun(l) returns the sum of both upper index and lower index

def eq_fun(l):
    s1, s2 = 0, 0
    for i in range(0, (len(l) // 2)):
        s1 = s1 + l[i]
    for i in range(len(l) // 2, len(l)):
        s2 = s2 + l[i]
    return s1,s2

#f(l) checks the sum of both upper and lower index to be equal or not.

def f(l):
    if len(l)%2==0:
        s1,s2=eq_fun(l)
    else:
        l.pop(len(l)//2)    #middle element is removed if len is odd
        s1,s2=eq_fun(l)
    print(f's1 is {s1} s2 is {s2}')
    if s1==s2:
        print('Equilibrium')
    else:
        print('Not eq')

f([12,12,12,1,6,18,12,12])