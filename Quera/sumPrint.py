# 275795 

n=int(input())

sum=0
if n ==1 : 
    print('1 = 1')
else :
    for i in range(1,n+1):
        sum+=i 
        if i < n : 
          print(i, '+' ,end=' ')
        else :
             print(i,'=' ,sum)