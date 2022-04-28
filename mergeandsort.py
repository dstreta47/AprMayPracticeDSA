def mergeandsort(lst1,lst2):
    i = 0
    j = 0
    k=0
    lst3 = [0,0,0,0,0,0,0,0,0]

    for i in range(len(lst1)+len(lst2)):
        lst3.append

    while i< len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            lst3[k] = lst1[i]
            i+=1
            k+=1
        else:
            lst3[k] = lst2[j] 
            j+=1
            k+=1

    return lst3        


test1 = [ 2,4,6,8]
test2 = [1,3,5,7,9]   

print(mergeandsort(test1,test2))
