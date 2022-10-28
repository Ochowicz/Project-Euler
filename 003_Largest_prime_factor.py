p = 600851475143  # our prime number
n = 2  # our potential factor
while n**2 < p:
    while p % n == 0:
        p = p / n
    n = n + 1
print(int(p))
