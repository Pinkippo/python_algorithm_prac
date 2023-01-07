x = list(input().split())
y = []

for i in x:
    if i == '(': y.append(i)
    elif i == ')': y.pop()
if len(y) > 0: print(False)
else: print(True)

