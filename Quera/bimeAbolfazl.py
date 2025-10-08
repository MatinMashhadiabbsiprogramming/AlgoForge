# 281772

txt=input()

for i in range(len(txt)):
    if txt[i] == "m":
        print('No')
        break
    if txt[i] == txt[-1]:
        print("Yes")