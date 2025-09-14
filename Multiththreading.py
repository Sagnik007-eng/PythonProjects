import threading as t
def fun(name):
    print(f'Name is {name}')

d1 = {i: f"number_{i}" for i in range(1, 1_000_001)}
if __name__=='__main__':
   thread_list = list()
   for i in d1:
       thread=t.Thread(target=fun,args=(d1[i],))
       thread_list.append(thread)
   for p in thread_list:
       p.start()
   for p in thread_list:
       p.join()
