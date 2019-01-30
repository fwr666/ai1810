num = 1
s = 0
print()
while num <= 100:
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        num += 1
        continue
    
    s += num
    num += 1
print(s)
