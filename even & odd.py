a=[23,12,2,6,4,8,5,99,34,65]
i=1
e=[]
o=[]
while i<len(a):
    if a[i]%2==0:
        e.append(a[i])
    else:
        o.append(a[i])
    i=i+1
print("even numbers",e) 
print("odd numbers",o) 