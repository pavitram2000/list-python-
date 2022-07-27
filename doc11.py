# a="9119"
# i=0
# while i<len(a):
#     b=int(a[i])**2
#     print(b,end=" ")
#     i+=1

a=[9,1,1,9]
i=0
b=""
while i<len(a):
    b=b+str(a[i]**2)
    i+=1
print(b)
