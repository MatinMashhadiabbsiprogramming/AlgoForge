# 655

n=int(input())
resultTxt=[]

for i in range(n):
    txt=input()
    a=txt.title()
    resultTxt.append(a)
for i in range(len(resultTxt)):
    print(resultTxt[i])