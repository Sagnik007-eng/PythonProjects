myList = [5, 7, 9, 11]
diff=myList[1]-myList[0]
for i in range(0,len(myList)):
    if myList[i + 1] == myList[-1]:
        break
    if myList[i+1]-myList[i]==diff:
        print('Sofasogood')
        continue
    else:
        print('Not in seq')
        break

