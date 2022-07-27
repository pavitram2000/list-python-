a=[20,37,20,21]
n=a
i=0
b=[]
while i<len(n):
    if a[i]not in b:
        b.append(a[i])
    i+=1
print(b)