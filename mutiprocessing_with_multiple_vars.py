import multiprocessing as mp
def fun(numbers,array_sq_list):
    i=0
    for n in numbers:
        array_sq_list[i]=n**3
        i=i+1
    print(array_sq_list[::])


if __name__=='__main__':
    numbers=[1,2,3,4,5]
    result=mp.Array('i',len(numbers))
    p=mp.Process(target=fun,args=(numbers,result))
    p.start()
    p.join()

    print(result[::])
