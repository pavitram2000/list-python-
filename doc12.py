a="1234567"
i=0
while i<len(a):
    j=len(a)-(i+1)
    b=int(a[i])*10**j
    print(b)
    i+=1