a=[[78,76,94,86,89],[91,71,98,65,76],[95,45,78,52,49]]
i=0
sum=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j+=1
    i+=1
print(sum)
