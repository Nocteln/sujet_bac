def binaire(a):
    bin_a = "0"
    a = a // 2
    while a != 0 :
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

print(binaire(83))
print(binaire(127))
print(binaire(0))