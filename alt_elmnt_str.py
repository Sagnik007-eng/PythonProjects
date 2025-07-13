#This program fetches elements of 2 strs and adds them 1 by 1. ex- if
# s1='abc' and s2='def' then I need to create a new str 'adbecf'


def fun(word1,word2):
    if len(word1) >len(word2):
       big_str=word1
       smal_str=word2
    else:
       big_str=word2
       smal_str=word1

    l=[]


    try:
        for i in range(0,len(big_str)):
            l.append(smal_str[i])
            l.append(big_str[i])
    except IndexError as e:
        for i in range(len(smal_str), len(big_str)):
            l.append(big_str[i])

    s1=''.join(l)
    print(s1)

fun('abcd','efgh')
