# problem 5 | Smallest Multiple


valid=True
a=21
listadd=[]
while valid==True:
    a+=1
    # for i in range(1,20):
    # if a%range(10,20)==0: 
    #     listadd.append(a)
        
            
    if a%1 == 0 and a%2==0 and a%3==0 and a%4==0 and a%5==0 and a%6 == 0 and a%7==0 and a%8==0 and a%9==0 and a%10==0 and a%11==0 and a%12==0 and a%13==0 and a%14==0 and a%15==0 and a%16 == 0 and a%17==0 and a%18==0 and a%19==0 and a%20==0 :
        valid=False
        listadd.append(a)
print(listadd)
        