A=[1,-3,2,-4,5,-6,7,-8]
B=[]
C=[]
i=0
while i<len(A):
    if A[i]>=0:
        B.append(A[i])
    else:
        C.append(A[i])
    i=i+1
print(B)
print(C)