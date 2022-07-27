num=[50,10,20,30,40,60,70,80,90]
max1=max(num)
max2=0
i=0
while i<len(num):
    if max2<num[i]:
        if num[i]!=max1:
            max2=num[i]
    i+=1
print(max2,"second maximum")