a=[1234,122,1984,19372,100]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]==a[j]:
            print("true")
        j+=1
    i+=1