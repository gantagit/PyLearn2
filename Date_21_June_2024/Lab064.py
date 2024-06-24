# Tuple - Collection of items

t1 = tuple()  # tuple() create an empty tuple
print(t1)

t2 = tuple(["Vijay", "Ganta", "Pramod"])  # converting a list to tuple
print(t2)

t5 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # tuple packing

t3 = tuple(t1)  # copying a tuple
print(t3)

t4 = tuple(t2)  # copying a tuple
print(t4)

t6 = tuple(t5)  # copying a tuple
print(t6)

del t1  # delete a tuple
print(t1) this will not print as the t1 tuple is already deleted
