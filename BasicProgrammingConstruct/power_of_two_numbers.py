'''
    @Name : Ronit kumar Patel
    @Title : Power of 2
'''

def power(num):
    result = 1
    for i in range(1,num+1):
        result *= 2
        print(f"\n2 ^ {i} = {result}")
num = int(input("Enter number you want find power of 2 : "))
p = power(num)
print(p)