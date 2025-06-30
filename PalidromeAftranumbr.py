def fun(num):
    while True:
       l = [i for i in str(num)]
       r = l[::-1]
       s = ''
       for i in r:
           s = s + i
       rev_num = int(s)
       if num==rev_num:
           print(f'Next palidrome is {num}')
           break
       num=num+1

fun(90)
