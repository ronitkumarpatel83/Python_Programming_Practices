"""
    @Name : Ronit kumar Patel
    @Title : Three largest number
"""


def three():
    f = int(input("Enter the first number : "))
    s = int(input("Enter the second number : "))
    t = int(input("Enter the third number : "))
    if f >= s and f >= t:
        print("the largest number is : ", f)
    elif s >= t:
        print("the largest number is : ", s)
    else:
        print("the largest number is : ", t)


three()
