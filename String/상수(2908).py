a,b = input().split()
reversed_a = a[::-1]
reversed_b = b[::-1]
reversed_a = int(reversed_a)
reversed_b = int(reversed_b)
if reversed_a > reversed_b:
    print(reversed_a)
else:
    print(reversed_b)