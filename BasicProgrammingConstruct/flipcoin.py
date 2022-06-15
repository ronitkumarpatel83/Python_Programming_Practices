import random
def coin():
    flip_coin = random.randint(0,1)
    if flip_coin == 0:
        #print("Head")
        return "head"
    else:
        #print("Tail")
        return "tail"
c = coin()
print('The display side is : '+c)