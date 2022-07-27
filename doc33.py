list=[12,67,98,34]
b=[]
i=0
while i<len(list):
    d=list[i]//10
    n=list[i]%10
    sum=d+n
    b.append(sum)
    i+=1
print(b)