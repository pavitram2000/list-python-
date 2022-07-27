a=[5,4,[1,2],6,[7,8],9]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    b.append(a[i][j][k])
                    k=k+1
            else:
                b.append(a[i][j]) 
                j=j+1
    else:
        b.append(a[i])
    i=i+1
print(b)
i=0
sum=0
while i<len(b):
    sum+=i
    i+=1
print(sum)                               

