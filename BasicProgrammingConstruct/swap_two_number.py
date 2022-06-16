"""
    @Name : Ronit kumar Patel
    @Title : Swap Two Number
"""


def swap(x, y):
    '''
    Number swapping without third variable
    :param x:
    :param y:
    :return: nothing
    '''
    print("Before swapping number a : ", x)
    print("Before swapping number b : ", y)
    x, y = y, x
    print("After swapping number a : ", x)
    print("After swapping number b : ", y)

a=int(input("Enter value : "))
b=int(input("Enter value : "))
swap(a, b)

