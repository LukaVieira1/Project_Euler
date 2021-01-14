value = 600851475143
prime = 2
while prime * prime < value:
    while value % prime == 0:
        value = value / prime
    prime = prime +1

print(value)
