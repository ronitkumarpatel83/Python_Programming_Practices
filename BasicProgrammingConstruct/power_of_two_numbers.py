'''
    @Name : Ronit kumar Patel
    @Title : Power of 2
'''


def power(number):
    result = 1
    for i in range(1, number + 1):
        result *= 2
        print(f"\n2 ^ {i} = {result}")


number = int(input("Enter number you want find power of 2 : "))
power(number)
