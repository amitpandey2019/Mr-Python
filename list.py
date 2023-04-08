a=[1,1,2,3,5,8,13,21,34,55,89]
b=[]
n=int(input("enter the limit"))
for i in a:
    if i<n:
        b.append(i)
        print(b)