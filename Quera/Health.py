# 51865

X = int(input())  
N = int(input())  

if N == 0:
    result = 20
elif N == 7:
    result = X
else:
    result = max(0, X - N)  

print(result)