#20249

n,k=map(int,input().split())
adad=list(map(int,input().split()))

sums=sum(adad)

# solutins is Time Limit Exceeded
sum2=n+k
while sums!=0: 
    sums -=k 
    n-=1

# this solutins is Time Limit Exceeded is solved:
# solutins ai
##stepes=(sums+k-1)//k
##n-=stepes
print(n)
