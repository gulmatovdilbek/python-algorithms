import math

S, P = map(int, input().split())
D = S*S - 4*P

if D < 0 or int(math.isqrt(D))**2 != D:
    print(-1)
else:
    x = (S + int(math.isqrt(D))) // 2
    y = S - x
    print(x, y)