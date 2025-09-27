#3405

listNumbers=[]

while True:
    a=int(input())
    if a!=0:
        listNumbers.append(a)
    else:
        break

for i in range(len(listNumbers)-1,-1,-1):
    print(listNumbers[i])
