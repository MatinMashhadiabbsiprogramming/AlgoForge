# 140032

a,b,c,d,e=map(int,input().split())

def Triangle(x,y,z):
    return x + y > z and x+z>y and y+z>x

if (
    Triangle(a,b,c) or 
    Triangle(a,b,d) or 
    Triangle(a,b,e) or 
    
    Triangle(a,c,d) or 
    Triangle(a,c,e) or 
    
    Triangle(a,d,e) or
    
    Triangle(b,c,d) or 
    Triangle(b,c,e) or 
    Triangle(b,d,e) or 
    Triangle(c,d,e) 

):
    print("YES")
else:
    print("No")

# if (a+b<c) or (a+b<d) or(a+b<e) or (a+c<b) or (a+c<d) or (a+c<e) or (a+d<b) or (a+d<c) or (a+d<e) or (a+e<b) or (a+e<d) or (a+e<e)  :
#     print("YSE")
# else:
#     print("NO")