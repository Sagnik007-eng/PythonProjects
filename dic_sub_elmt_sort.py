# Input is -->employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
#The output should be: [('Diana', ('NYC', 3500, 31)), ('Maria', ('Zagreb', 3800, 40)), ('John', ('London', 4000, 28))]



employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}

l=sorted(employees.items(),key=lambda x:x[1][1])
print(l)