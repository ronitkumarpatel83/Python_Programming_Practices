def factorial_number(n):
    if n == 0:
        return 1
    else:
        print("X",+n)
        return n * factorial_number(n - 1)

n = int(input("Enter the factiorial number : "))
print(factorial_number(n))