# list Functions Scope and Lifetime

list_1 = [1, 2, 3, 4]
list_2 = [1, 2, "Vijay", 3.14]

list_1.append(4)
print(list_1)

list_1.extend([5, 6])
print(list_1)

list_1.insert(3, 9)
print(list_1)

list_1.sort()
print(list_1)

list_1.reverse()
print(list_1)

list_1.extend(list_2)
print(list_1)

list_2.remove("Vijay")
print(list_2)

list_3 = list_1.copy()
print(list_3)

list_1.pop()
print(list_1)

list_1.clear()
print(list_3)
