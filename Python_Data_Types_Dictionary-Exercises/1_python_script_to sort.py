import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Main Dictionary : ',d)
sorted_dict = sorted(d.items(), key=operator.itemgetter(1))
print('Ascending order by value : ',sorted_dict)
sorted_dict = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Descending order by value : ',sorted_dict)