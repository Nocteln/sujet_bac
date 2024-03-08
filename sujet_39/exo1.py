def fibonacci(x):
    if x == 0 or x ==1:
        return x
    else:
        return fibonacci(x-2) + fibonacci(x-1)

print(fibonacci(25))