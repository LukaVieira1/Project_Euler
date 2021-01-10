nums = []
a, b = 1, 2
while b <= 4000000:
    if b % 2 ==0:
       nums.append(b)
    a, b = b, a + b
print(sum(nums))








