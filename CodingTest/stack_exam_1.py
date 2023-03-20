x = list(input().split())
y = []
z = []

for i in x:
    if i == "(":
        y.append(i)
    elif i == ")":
        z.append(i)

if len(y) == len(z):
    print(True)
else:
    print(False)

