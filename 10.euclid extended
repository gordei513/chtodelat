a = int (input("Введите 1-ое число:"))
b = int (input("Введите 2-ое число:"))

def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        div, x, y = gcd(b % a, a)
    return (div, y - (b // a) * x, x)
c = gcd(a, b)
print(f'gsd ={c[0]} ;  q = {c[1]}  p = {c[2]}')
