#283

a = int(input())
b = int(input())
if a<=b:
    print("Wrong order!")

if (a-b)%2!=0:
    print("Wrong difference!")
    
else:
    start = (a - b) // 2  
    end = start + b      

    for i in range(a):
        for j in range(a):
            if start <= i < end and start <= j < end:
                print(" ", end=" ")  
            else:
                print("*", end=" ")  
        print()  
