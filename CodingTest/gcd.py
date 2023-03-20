def gcd(a,b): #gcd 뺴기
    while a != 0 and b!= 0:
        if a>b: a =  a-b
        else: b = b-a
    return a + b

def gcd2(a,b): #gcd_mod
    if a>b:
        a = a % b
        if a == 0:
            return b
        else:
            return a
    else:
        b = b % a
        if b == 0:
            return a
        else: 
            return b


x = gcd(4,12)
print(x)