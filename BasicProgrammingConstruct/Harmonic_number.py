def sum(n):
    i = 1
    s = 0.0
    for i in range(1, n + 1):
        s = s + 1 / i
        print(f'1/{i}+')
    return s
n = int(input('Enter the number : '))
print(f'The harmonic number {n} is : {sum(n)}')