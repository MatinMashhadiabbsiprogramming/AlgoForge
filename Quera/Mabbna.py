# 594
a,b=map(int,input().split())

def ConvertNum(N1,N2):
    result = ''
    while N2<N1:
        result+=str(N1%N2)
        N1=N1 // N2
    result+=str(N1)
    return result[::-1]
objects=(ConvertNum(a,b))
sum1=0
sum2=0
for i in objects[::2]:
    sum1+=int(i)
for i in objects[1::2]:
    sum2+=int(i)
if sum1 == sum2:
    print("Yes")
else: 
    print("No")
# print(sum1,sum2)