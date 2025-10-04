# 280
a=int(input())
b=int(input())
c=int(input())

if a!=0 and b!=0 and c!=0:
    x,y,z=sorted([a,b,c])
    if x**2 + y**2 == z**2: 
        print("YES")
    else:
        print("NO")
else:
    print("NO")