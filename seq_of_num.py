# Write a Python script that displays the following pattern from 1 to n where n is entered by the user.
#
# If the user enters 6 it will display:
#
# 1
# 22
# 333
# 4444
# 55555
# 666666


num=int(input('Entr num'))
for i in range(1,num):
    print(str(i)*i)