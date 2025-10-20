# 593
def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
b = sum_of_digits(n)

count = 0
candidate = n + 1

while True:
    if is_prime(candidate):
        count += 1
        if count == b:
            print(candidate)
            break
    candidate += 1
