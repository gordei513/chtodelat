a=32
b=73
c=32
def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        div, x, y = gcd(b % a, a)
    return (div, y - (b // a) * x, x)
c = gcd(a, b)
