a = int (input("Введите 1-ое число:"))
b = int (input("Введите 2-ое число:"))
def gcdn(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
        return a+b
print (gcdn(a,b))
