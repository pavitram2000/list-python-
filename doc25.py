a=[4,6,4,3,3,4,3,4,3,8]
k=3
i=0
count=0
while i<len(a):
    if a[i]==k:
        count+=1
    i+=1
print(count,k)