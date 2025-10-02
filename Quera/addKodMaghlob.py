#617
numInput=input()
result=''
for i in range(len(numInput)-1,-1,-1) :
    result+=numInput[i] 
else:
    if int(numInput) == int(result):
        print('YES')
    else:
        print('NO') 