# 218361
a=list(map(int,input().split()))
b=list(map(int,input().split()))

counter=0

for i in range(8):
    if a[i] == 1 and b[i]==1:
        counter+=1
        continue
print(counter)