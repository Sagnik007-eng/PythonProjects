def primetest(x):
   for i in range(2,x-1):
       if x%i==0:
           #print(f"{x} is div by {i} so {x} its not prime")
           break
       else:
           continue
   else:
       print(f"{x} is prime")

for i in range(3,35):
    primetest(i)