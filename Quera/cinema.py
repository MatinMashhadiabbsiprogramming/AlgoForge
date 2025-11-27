# 235328

n,k=map(int,input().split())
friend=list(map(int,input().split()))

g_size=[1 + x for x in friend]
print(g_size)
g_size.sort()
print(g_size)

total = 0
count = 0

for i in range(n):
    if total + g_size[i] <= k :
        total += g_size[i]
        count+=1
    else:
        break

print(count)