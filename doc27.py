# a=[1,2,3]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if a[i]!=a[j] and a[j]!=a[k] and a[k]!=a[i]:
#                 print(a[i],a[j],a[k])
#             k=k+1
#         j=j+1
#     i=i+1


a=[0,9,5]
for i in a:
    for j in a:
        for k in a:
            if i!=j and j!=k and i!=k and j!=i and k!=i and k!=j:
                print(i,j,k)