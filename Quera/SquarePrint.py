# 591
n=int(input())

star='*'
print(star*n)
for i in range(n-2):
    print(star+' '*(n-2)+star)
print(star*n)
