#Write a Python script that checks if a
# triangle is equilateral, isosceles or scalene.


x=int(input('Enter x'))
y=int(input('Enter y'))
z=int(input('Enter z'))

if x==y:
    if y==z:
        print('Triangle is equilateral')
    else:
        print('Isocles')

else:
    if y==z:
        print('Isocles')
    elif x!=y and y!=z and x==z:
        print('Isocles')
    else:
        print('Scaline')
