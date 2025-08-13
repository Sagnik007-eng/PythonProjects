words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom' ]

wrd_pal=[i for i in words if i[::-1].lower()==i.lower()]
print(wrd_pal)