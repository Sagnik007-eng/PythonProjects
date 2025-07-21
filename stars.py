#Want a star pattern as follows
# *
#
# * *
#
# * * *
#
# * * * *
#
# * * * * *
#
# * * * *
#
# * * *
#
# * *
#
# *
def fun_stars(n):
    for i in range(1, n):
        print('*' * i)
    i = i - 1
    for j in range(i, 0, -1):
        print('*' * j)