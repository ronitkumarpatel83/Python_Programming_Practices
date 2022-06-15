# Sets take only unique element
s = set()
# print(type(s)) # it is set type
# n = [1,2,3,4,5,6,5]
# list = set(n)
# print(list) # it is also set but it is look like list
# print(type(list))
s.add(2)
# s.add(2) # cause set takes only unique value only
s.add(1)
# s.union({1,2,3}) # in union takes only same element
print(s)

#tuples is like list but list is mutable and tuple immutable

t = (21,32,34,56)
print(t) #tuple's cannot be change value