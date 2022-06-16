"""
    @Name : Ronit kumar Patel
    @Title : Quotient and remainder
"""


def Quotient(div, divis):
    q = divis / div
    print(q)


def Remainder(div, divis):
    q = divis % div
    print(q)


div = int(input("Please enter dividend : "))
divis = int(input("Please enter divisor : "))
Quotient(div, divis)
Remainder(div, divis)
