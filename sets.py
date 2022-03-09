mi_set = set([1, 2, 3, 5, (1, 1, 1, 1)])
print(type(mi_set))
print(len(mi_set))

set_one, set_two = {1, 2, 3}, {3, 4, 5}
set_three = set_one.union(set_two)
set_three.add(6)
set_three.clear()
print(set_three)