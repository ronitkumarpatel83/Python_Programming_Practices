"""
    @Name : Ronit kumar Patel
    @Title : Three largest number
"""


def three():
    first = int(input("Enter the first number : "))
    second = int(input("Enter the second number : "))
    third = int(input("Enter the third number : "))
 #   if first >= second and first >= third:
    if second < first > third :
        print("the first is the greatest number : ", first)
    elif second >= third:
        print("the second is the greatest number : ", second)
    else:
        print("the third is the greatest number : ", third)


three()
