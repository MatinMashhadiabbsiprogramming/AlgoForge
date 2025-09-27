# problem 1 | Multiples of 3 or 5 

value = 1000 
count=0
listMutiples=[]

for i in range(1,value):
    if (i%3 ==0 ) or (i%5==0):
        count+=i
        listMutiples.append(i)
        
print(f'list of multiples of 3 and 5 is:{listMutiples}')
print(f"sum of mutiples is : {count}")