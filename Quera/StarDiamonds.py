# 9773
n=int(input())
tu=1
for i in range(1,n+1,2):
    
    s='*'*i
    # result=' '*(int((n/2))-tu)+ s+' '*((n-(2*i+1))//2)+' '*(int((n/2))-tu) + s
    result=' '*(int((n/2))-tu)+ s+' '*(int((n/2)+1)-tu)
    result = result*2
    print(result)
    tu+=1 
tu2=1
for i in range(n-2,-1,-2):
    s='*'*i
    result=' '*((tu2)-1)+ s+' '*(tu2)
    result = result*2
    print(result)
    tu2+=1