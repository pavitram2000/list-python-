a=[2,-7,-5,-64,-14]
i=0
count=0
count1=0
b=[]
c=[]
while i<len(a):
    if a[i]>0:
        count+=1
        b.append(a[i])
    else:
        count1+=1
        c.append(a[i])
    i+=1
print("positive number",count,b)
print("negative number",count1,c)