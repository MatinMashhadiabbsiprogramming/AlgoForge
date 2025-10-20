# 3432
n,m=map(int,input().split())

timeMj=list(map(int,input().split()))
timeMostafa=list(map(int,input().split()))


# timeMj.sort()
# timeMostafa.sort()
def is_subset(a, b):
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
            
        elif a[i] > b[j]:
            j += 1
            
        else:
            return False
    return i == len(a)

if timeMj == timeMostafa:
    print("Both")
    
elif is_subset(timeMj, timeMostafa):
    print("Mohammad Javad")
    
elif is_subset(timeMostafa, timeMj):
    print("Mostafa")
else:
    print("None")