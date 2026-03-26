n = int(input())

y = 0

for son in range(1, n + 1):
    
  if son % 3 == 0 or son % 5 == 0 or son % 7 == 0:
         y += son

print(y)