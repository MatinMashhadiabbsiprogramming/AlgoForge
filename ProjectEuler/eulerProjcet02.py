# problem 2 | Even Fibonacci Numbers

continueS = 4000000
a=1
b=2
Sum_fib_Even=0
while a<= continueS:
    if a %2 ==0 :
        Sum_fib_Even +=a
    a,b=b,a+b
    
print("sum of Even fibonacci numbers 4mil",Sum_fib_Even)