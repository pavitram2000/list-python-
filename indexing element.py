a=[[1,2,3],[4,5,6],[7,8,9]]
i=0
while i<len(a):
    j=0
    while j<len(a):
        print(a[i][j],"=",i,j)
        j+=1
    i+=1