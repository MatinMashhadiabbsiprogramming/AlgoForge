# 235327

t=int(input())
res=[]
for i in range(t):
    a,b,h=map(int,input().split())
    
    if a>=h: 
        res.append(1)
        continue
    
    c=0
    days=0
    while True:
        days+=1
        c+=a
        if c>=h:
            res.append(days)
            break
        c-=b
print("\n".join(map(str,res)))