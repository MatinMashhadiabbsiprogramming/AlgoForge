# 293 

a=int(input())
b=int(input())

for i in range(a,b+1):
    if i < 2  : 
        continue
    prime=True
    for j in range(2,i):
        if i % j ==0 : 
            prime= False
            break
    if prime: print(i)