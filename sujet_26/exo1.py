def multiplication(n1, n2):
    res= 0
    a=n1
    b=n2
    if n1 == 0 or n2 == 0:
        return 0
    if n1 < 0:
        a = -n1
    if n2 < 0:
        b = -n2
    for _ in range(a):
        res += b
    if n1 < 0:
        res = -res
    if n2 < 0:
        res = -res
    return res
print(multiplication(-3,5))