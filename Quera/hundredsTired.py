#3406

a=input()
b=input()

repa=a[::-1]
repb=b[::-1]
if int(repa)==int(repb):
    print(f"{a} = {b}")
    exit()
if int(repa) < int(repb):
    print(f"{a} < {b}")
else:
    print(f"{b} < {a}")
    
